# Modified from https://github.com/pytorch/examples/blob/master/fast_neural_style/neural_style/
# The main changes are conditional instance normalization logic 
import torch

class TransformerNet(torch.nn.Module):
    def __init__(self, style_num):
        super(TransformerNet, self).__init__()         #torch.nn.Module 상속 
        self.conv1 = ConvLayer(3, 32, kernel_size = 9, stride = 1)   #stride가 1이므로 입력 이미지와 출력이미지의 차원이 같음 
        self.in1 = ConditionalInstanceNorm2d(style_num, 32)

        self.conv2 = ConvLayer(32, 64, kernel_size = 3, stride = 2) #stride가 2이므로 출력 이미지의 가로 및 세로 차원이 입력 이미지의 절반으로 축소됨. 이로 인해  더 작은 공간 차원에서 이미지 특징을 추출하고 더 많은 정보를 다룰 수 있게 됨
        self.in2 = ConditionalInstanceNorm2d(style_num, 64)

        self.conv3 = ConvLayer(64, 128, kernel_size = 3, stride = 2)  #입력 이미지를 다운샘플링하고, 더 높은 수준의 추상적인 정보를 학습하는 데 도움을 줌. 스타일 변환 작업에 있어서 이미지의 구조 및 스타일을 고려하는 데 유용
        self.in3 = ConditionalInstanceNorm2d(style_num, 128)

        self.res1 = ResidualBlock(128)
        self.res2 = ResidualBlock(128)
        self.res3 = ResidualBlock(128)
        self.res4 = ResidualBlock(128)
        self.res5 = ResidualBlock(128)
        self.deconv1 = UpsampleConvLayer(128, 64, kernel_size = 3, stride = 1, upsample = 2)
        self.in4 = ConditionalInstanceNorm2d(style_num, 64)
        self.deconv2 = UpsampleConvLayer(64, 32, kernel_size = 3, stride = 1, upsample = 2)
        self.in5 = ConditionalInstanceNorm2d(style_num, 32)
        self.deconv3 = ConvLayer(32, 3, kernel_size = 9, stride = 1)
        self.relu = torch.nn.ReLU()

    def forward(self, X, style_control):             #nn.Module을 상속 받았기 때문에 forward는 따로 호출하지 않아도 알아서 호출됨.
 
        y = self.relu(self.in1(self.conv1(X), style_control))
        y = self.relu(self.in2(self.conv2(y), style_control))
        y = self.relu(self.in3(self.conv3(y), style_control))
        y = self.res1(y)
        y = self.res2(y)
        y = self.res3(y)
        y = self.res4(y)
        y = self.res5(y)
        y = self.relu(self.in4(self.deconv1(y), style_control))
        y = self.relu(self.in5(self.deconv2(y), style_control))
        y = self.deconv3(y) 
        
        return y

class ConditionalInstanceNorm2d(torch.nn.Module):
    """
    Conditional Instance Normalization
    introduced in https://arxiv.org/abs/1610.07629
    """
    def __init__(self, style_num, in_channels):
        super(ConditionalInstanceNorm2d, self).__init__()
        self.condInstanceNorm = torch.nn.ModuleList()
        # 서로 다른 스타일에 대한 InstanceNorm2d 모듈들을 리스트로 초기화
        for i in range(style_num):
            self.condInstanceNorm.append(torch.nn.InstanceNorm2d(in_channels, affine=True))
        #인스턴스 정규화는 각 입력 샘플에 대해 정규화를 수행하므로 배치 크기에 상관없이 동작 # 특정 영역에 몰려 있는 경우 화질을 개선하기도 하고, 이미지 간의 연산 시 서로 조건이 다른 경우 같은 조건으로 만듬
    def forward(self, x, style_control):
        out = []
        # 각 이미지에 대한 조건부 인스턴스 정규화 수행
        for i in range(x.shape[0]):
            total_weight = 0
            out_xi = x[i].clone().fill_(0)
            # 이미지의 각 채널에 대해 서로 다른 스타일을 가중합하여 적용
            for j in range(len(style_control[i % len(style_control)])): #모든 이미지에 대해 서로 다른 스타일을 적용하거나, 스타일 컨트롤 리스트의 길이가 이미지 수보다 많은 경우 중복된 스타일을 적용할 수 있음
                total_weight += style_control[i % len(style_control)][j] #현재 스타일의 가중치를 전체 가중치에 더함.
                # 해당 채널의 InstanceNorm2d를 스타일 가중치와 함께 적용
                out_xi += style_control[i % len(style_control)][j] * self.condInstanceNorm[j](x[i].unsqueeze(0)).squeeze_(0)   #unsqueeze와 squeeze를 왜 둘다 했는지는 잘 모르겠음 
            # 채널별 가중 평균을 통해 이미지 완성 # 현재 스타일의 채널별 가중치를 해당 이미지의 채널에 적용합니다. condInstanceNorm[j]는 j번째 스타일의 조건부 인스턴스 정규화 레이어를 나타냅니다. 이 레이어는 현재 이미지의 해당 채널에 대해 스타일을 조절합니다.
            out.append(out_xi / total_weight)  # 각 이미지의 각 채널에 대해 서로 다른 스타일을 가중합하여 적용했기 때문에 total_weight으로 나눠줌
        out = torch.stack(out)
        return out
    
    
class ConvLayer(torch.nn.Module):

    def __init__(self, in_channels, out_channels, kernel_size, stride):
        super(ConvLayer, self).__init__()
        # Reflection padding을 사용하여 경계 효과를 고려한 Conv2d 레이어 초기화
        #주어진 이미지 주변을 반사하여 이미지의 경계를 확장하는데, 이때 경계 확장된 부분은 입력 이미지의 픽셀 값을 반전하여 채워넣음. 이렇게 하면 경계 부분에서 컨볼루션 연산을 수행할 때 정보가 더 잘 보존됨.
        reflection_padding = kernel_size // 2 #커널의 반 크기로 이미지 경계 확장 
        self.reflection_pad = torch.nn.ReflectionPad2d(reflection_padding)
        self.conv2d = torch.nn.Conv2d(in_channels, out_channels, kernel_size, stride)

    def forward(self, x):     #x는 Transformernet의 객체를 생성한 후 생성한 객체에 이미지를 넣어주면 자동으로 들어옴 다른 함수도 마찬가지 
        # Reflection padding과 Conv2d 연산을 통해 출력 생성
        out = self.reflection_pad(x)
        out = self.conv2d(out)
        return out


class ResidualBlock(torch.nn.Module):  #네트워크의 깊이를 깊게 만들면서도 그래디언트 소실 문제를 해결하는 데 도움 
    #입력과 출력 사이에 skip connection(또는 shortcut connection)을 추가하여 네트워크에서 특정 레이어를 건너뛰는 구조를 갖고 있음
    """ResidualBlock
    introduced in: https://arxiv.org/abs/1512.03385
    recommended architecture: http://torch.ch/blog/2016/02/04/resnets.html
    """

    def __init__(self, channels):
        super(ResidualBlock, self).__init__()
        # 두 개의 ConvLayer와 InstanceNorm2d, ReLU를 포함하는 Residual Block 초기화
        self.conv1 = ConvLayer(channels, channels, kernel_size=3, stride=1)
        self.in1 = torch.nn.InstanceNorm2d(channels, affine=True)  #신경망이 훈련 중에 스케일과 시프트 파라미터를 조정하여 데이터를 더 잘 표현할 수 있도록 도와즘
        #스케일(scale): 각 채널의 출력에 곱해지는 파라미터입니다. 스케일을 학습할 수 있으면, 네트워크가 각 채널의 중요도나 활성화를 더 잘 조절할 수 있습니다.
        #시프트(shift): 각 채널의 출력에 더해지는 파라미터입니다. 시프트를 학습할 수 있으면, 각 채널의 평균 값을 조절하거나 이동할 수 있습니다.
        self.conv2 = ConvLayer(channels, channels, kernel_size=3, stride=1)
        self.in2 = torch.nn.InstanceNorm2d(channels, affine=True)
        self.relu = torch.nn.ReLU()

    def forward(self, x):
        residual = x
        # Residual Block 내에서의 순전파
        out = self.relu(self.in1(self.conv1(x)))
        out = self.in2(self.conv2(out))
        out = out + residual  # 잔여 연결 #네트워크의 일부 레이어에서 입력을 출력에 직접적으로 더해주는 기법
        # 네트워크의 깊이가 깊어질수록 발생하는 그래디언트 소실 문제를 완화하고, 더 깊은 네트워크에서도 효율적인 학습을 돕는 역할
        return out


class UpsampleConvLayer(torch.nn.Module):
    """UpsampleConvLayer
    Upsamples the input and then does a convolution. This method gives better results
    compared to ConvTranspose2d.
    ref: http://distill.pub/2016/deconv-checkerboard/
    """

    def __init__(self, in_channels, out_channels, kernel_size, stride, upsample=None):
        super(UpsampleConvLayer, self).__init__()
        self.upsample = upsample
        # 업샘플링 레이어 초기화
        if upsample:
            self.upsample_layer = torch.nn.Upsample(mode='nearest', scale_factor=upsample)
        # Reflection padding을 사용하여 업샘플링 중 나타날 수 있는 아티팩트 감소
        reflection_padding = kernel_size // 2
        self.reflection_pad = torch.nn.ReflectionPad2d(reflection_padding)
        self.conv2d = torch.nn.Conv2d(in_channels, out_channels, kernel_size, stride)

    def forward(self, x):
        x_in = x
        # 업샘플링이 지정된 경우 Upsample 레이어를 사용하여 입력을 업샘플링
        if self.upsample:
            x_in = self.upsample_layer(x_in)      #입력 데이터의 복사본을 저장하는 변수 #업샘플링이 지정된 경우 업샘플링된 입력을 저장
        # Reflection padding과 Conv2d 연산을 통해 출력 생성
        out = self.reflection_pad(x_in)
        out = self.conv2d(out)
        return out