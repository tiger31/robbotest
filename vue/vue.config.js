const path = require('path');
const CopyPlugin = require('copy-webpack-plugin');

module.exports = {
	outputDir: path.resolve(__dirname, "../robbotest/static/js/src/"),
	productionSourceMap: false,
	configureWebpack: {
		plugins: [
			new CopyPlugin([
				{ from: 'public/init.js', to: `test.js` },
				{ from: 'public/init_editor.js', to: `test_editor.js` }
			]),
		],
	},
};
