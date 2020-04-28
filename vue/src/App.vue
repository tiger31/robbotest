<template>
  <HelloWorldEditor url="123"/>
</template>

<script>
import HelloWorldEditor from "./components/HelloWorldEditor";

export default {
  name: 'App',
  components: {
		HelloWorldEditor,
  }
}
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
