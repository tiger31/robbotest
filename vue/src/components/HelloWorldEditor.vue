<template>
  <div class="hello">
    <span>Question:</span>
    <input v-model="settings.question" type="text" name="answer"/>
    <span>Answer:</span>
    <input v-model="settings.answer" type="text" name="answer"/>
    <button @click="assert">Save</button>
  </div>
</template>

<script>
  import axios from 'axios';
	export default {
		name: "HelloWorldEditor",
		props: {
			url: String,
      question: String,
      answer: String
		},
		data: function() {
			return {
        settings: {
          question: this.question,
          answer: this.answer,
        },
        cookies: {}
      }
		},
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
						question: this.settings.question,
            answer: this.settings.answer
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

<style scoped>

</style>