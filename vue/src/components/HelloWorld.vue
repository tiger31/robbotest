<template>
  <div class="hello">
    <span>{{question}}</span>
    <input v-model="value" type="number" name="answer"/>
    <button @click="assert">Check</button>
  </div>
</template>

<xblock url="{{self.url}}"></xblock>

<script>
import axios from 'axios';
export default {
  name: 'HelloWorld',
  props: {
    url: String,
    question: String
  },
  data: () => ({
    value: "",
    cookies: {}
  }),
  methods: {
    assert() {
      axios({
        baseURL: window.location.origin,
        url: this.url,
        method: 'post',
        headers: {
					'X-CSRFToken': this.cookies["csrftoken"],
          'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8"
        },
        data: JSON.stringify({
          answer: this.value
        })
      })
    }
  },
  mounted() {
    this.cookies = document.cookie.split(";").reduce((o, c) => {
      const [key, value] = c.split('=');
      o[key.trim()] = value;
      return o
    }, {})
	}
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
</style>
