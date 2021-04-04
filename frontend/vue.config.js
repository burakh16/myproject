module.exports = {
  pluginOptions: {
    quasar: {
      importStrategy: "kebab",
      rtlSupport: false,
    },
  },
  transpileDependencies: ["quasar"],
  lintOnSave: false  ,
  // assetsDir must match Django's STATIC_URL
  assetsDir: 'static',
};
