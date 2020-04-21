require.config({
  paths: { vue: 'https://cdnjs.cloudflare.com/ajax/libs/vue/2.6.11/vue.runtime.min' }
});
require(['vue'], function(data) {
  console.log(data)
  window.Vue = data
});

