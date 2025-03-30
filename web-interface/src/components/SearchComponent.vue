<template>
    <div class="search-container">
      <h1>Buscar Cadastros de Operadoras</h1>
      <div class="search-form">
        <select v-model="selectedColumn">
          <option v-for="column in columns" :key="column" :value="column">{{ column }}</option>
        </select>
        <input v-model="query" placeholder="Digite o termo de busca (inclua a data no formato YYYY-MM-DD para buscar por data)" />
        <button @click="search">Buscar</button>
      </div>
      <ul class="search-results">
        <li v-for="result in results" :key="result.Registro_ANS">
          <div><strong>Registro ANS:</strong> {{ result.Registro_ANS }}</div>
          <div><strong>Razão Social:</strong> {{ result.Razao_Social }}</div>
          <div><strong>Modalidade:</strong> {{ result.Modalidade }}</div>
          <div><strong>Cidade:</strong> {{ result.Cidade }}</div>
          <div><strong>UF:</strong> {{ result.UF }}</div>
          <div><strong>DDD:</strong> {{ result.DDD }}</div>
          <div><strong>Telefone:</strong> {{ result.Telefone }}</div>
        </li>
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
  .search-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    background-color: #f0f8f5;
    padding: 20px;
    border-radius: 10px;
    max-height: 80vh;
    overflow-y: auto;
  }
  
  .search-form {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 10px;
    margin-bottom: 20px;
  }
  
  .search-form select,
  .search-form input {
    padding: 10px;
    border: 1px solid #4CAF50;
    border-radius: 5px;
    width: 300px;
  }
  
  .search-form button {
    padding: 10px 20px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  
  .search-form button:hover {
    background-color: #45a049;
  }
  
  .search-results {
    list-style: none;
    padding: 0;
    width: 100%;
    max-width: 600px;
  }
  
  .search-results li {
    border: 1px solid #4CAF50;
    border-radius: 8px;
    padding: 10px;
    margin-bottom: 10px;
    background-color: #e8f5e9;
  }
  
  .search-results div {
    margin-bottom: 5px;
  }
  </style>