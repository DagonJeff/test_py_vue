<template>
    <div>
      <h1>Buscar Cadastros de Operadoras</h1>
      <select v-model="selectedColumn">
        <option v-for="column in columns" :key="column" :value="column">{{ column }}</option>
      </select>
      <input v-model="query" placeholder="Digite o termo de busca (inclua a data no formato YYYY-MM-DD para buscar por data)" />
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
        selectedColumn: 'Razao_Social',
        columns: [
          'Registro_ANS', 'CNPJ', 'Razao_Social', 'Nome_Fantasia', 'Modalidade', 'Logradouro',
          'Numero', 'Complemento', 'Bairro', 'Cidade', 'UF', 'CEP', 'DDD', 'Telefone', 'Fax',
          'Endereco_eletronico', 'Representante', 'Cargo_Representante', 'Regiao_de_Comercializacao', 'Data_Registro_ANS'
        ],
        query: '',
        results: []
      };
    },
    methods: {
      async search() {
        try {
          const queryParams = new URLSearchParams();
          if (this.query) {
            queryParams.append('query', this.query);
            queryParams.append('column', this.selectedColumn);
          }
  
          const response = await fetch(`http://127.0.0.1:5000/search?${queryParams.toString()}`);
          if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
          }
          const data = await response.json();
          console.log(data); 
          this.results = data;
        } catch (error) {
          console.error('Failed to fetch:', error);
        }
      }
    }
  };
  </script>
  
  <style scoped>
  /* Adicione o estilo necessário aqui */
  </style>