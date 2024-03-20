const path = require('path');
module.exports = {
    entry : './src/index.js',
    output : {
        path : path.resolve(__dirname, 'dist'),
        filename: 'bundle.js'
    },
    mode: 'development',
    devServer: {
        static: {
          directory: path.join(__dirname, 'dist'), // statik dosyaların bulunduğu dizini buraya belirtin
        },
    },
    module: {
        rules: [
          {
            test: /\.js$/,
            loader: 'babel-loader',
            exclude: /node_modules/
          },
          {
            test: /\.scss$/,
            use: [ 'style-loader','css-loader', 'sass-loader']
          }
        ]
      }      
}