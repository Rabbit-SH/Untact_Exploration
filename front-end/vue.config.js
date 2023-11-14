const { defineConfig } = require('@vue/cli-service');

module.exports = defineConfig({
    configureWebpack: {
        optimization: {
            splitChunks: {
                chunks: 'all'
            }
        }
    },
    transpileDependencies: [
      'vuetify'
    ],
    // publicPath: '/REMEMBER',
});
