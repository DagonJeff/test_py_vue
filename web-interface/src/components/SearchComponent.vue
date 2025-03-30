<template>
    <div>
      <h1>Buscar Cadastros de Operadoras</h1>
      <input v-model="query" placeholder="Digite o termo de busca" />
      <button @click="search">Buscar</button>
      <ul>
        <li v-for="result in results" :key="result.Registro_ANS">{{ result.Nome_Fantasia }}</li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        query: '',
        results: []
      };
    },
    methods: {
      async search() {
        const response = await fetch(`http://localhost:5000/search?query=${this.query}`);
        this.results = await response.json();
      }
    }
  };
  </script>