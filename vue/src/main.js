import Vue from 'vue'
import XBlock from './components/HelloWorld.vue'

Vue.config.productionTip = false;
new Vue({
  render: h => h(XBlock),
}).$mount('vue-foo-hello-world');
