<template>
  <div id="app">
    <SearchComponent />
  </div>
</template>

<script>
import SearchComponent from './components/SearchComponent.vue';

export default {
  name: 'App',
  components: {
    SearchComponent
  }
};
</script>

<style>

body {
  font-family: Arial, sans-serif;
  background-color: #e0f7fa;
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}
</style>