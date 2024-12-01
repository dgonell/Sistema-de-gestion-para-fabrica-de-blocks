<template>
    <div>
      <h1>Lista de Clientes</h1>
      <ul>
        <li v-for="cliente in clientes" :key="cliente.id">
          {{ cliente.nombre }} - {{ cliente.cedula_rnc }}
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import api from "../services/api";
  
  export default {
    data() {
      return {
        clientes: [],
      };
    },
    mounted() {
      api.get("/clientes")
        .then(response => {
          this.clientes = response.data;
        })
        .catch(error => {
          console.error("Error:", error);
        });
    },
  };
  </script>
  