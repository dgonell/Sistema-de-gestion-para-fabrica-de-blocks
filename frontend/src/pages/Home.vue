<template>
    <div class="p-8 bg-gray-50">
      <!-- Título -->
      <header class="mb-6">
        <h1 class="text-3xl font-bold text-gray-800">Bienvenido al Sistema de Blocks</h1>
        <p class="text-gray-600 mt-2">
          Administra clientes, producción, almacén y ventas de manera eficiente.
        </p>
      </header>
  
      <!-- Resumen de Estadísticas -->
      <section class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <!-- Clientes -->
        <div class="bg-white shadow-lg rounded-lg p-6">
          <div class="flex items-center space-x-4">
            <span class="material-icons text-blue-500 text-4xl">person</span>
            <div>
              <h2 class="text-2xl font-bold text-gray-800">120</h2>
              <p class="text-gray-500">Clientes Registrados</p>
            </div>
          </div>
        </div>
  
        <!-- Almacén -->
        <div class="bg-white shadow-lg rounded-lg p-6">
          <div class="flex items-center space-x-4">
            <span class="material-icons text-green-500 text-4xl">inventory</span>
            <div>
              <h2 class="text-2xl font-bold text-gray-800">4500</h2>
              <p class="text-gray-500">Blocks en Almacén</p>
            </div>
          </div>
        </div>
  
        <!-- Ventas -->
        <div class="bg-white shadow-lg rounded-lg p-6">
          <div class="flex items-center space-x-4">
            <span class="material-icons text-red-500 text-4xl">shopping_cart</span>
            <div>
              <h2 class="text-2xl font-bold text-gray-800">$25,000</h2>
              <p class="text-gray-500">Ventas Totales</p>
            </div>
          </div>
        </div>
      </section>
  
      <!-- Acciones Rápidas -->
      <section class="mt-8">
        <h2 class="text-xl font-semibold text-gray-800 mb-4">Acciones Rápidas</h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <router-link
            to="/clientes"
            class="bg-blue-500 text-white rounded-lg shadow-md p-6 flex items-center justify-between hover:bg-blue-600 transition"
          >
            <span class="text-lg font-semibold">Gestionar Clientes</span>
            <span class="material-icons text-3xl">arrow_forward</span>
          </router-link>
          <router-link
            to="/produccion"
            class="bg-green-500 text-white rounded-lg shadow-md p-6 flex items-center justify-between hover:bg-green-600 transition"
          >
            <span class="text-lg font-semibold">Registrar Producción</span>
            <span class="material-icons text-3xl">arrow_forward</span>
          </router-link>
          <router-link
            to="/ventas"
            class="bg-red-500 text-white rounded-lg shadow-md p-6 flex items-center justify-between hover:bg-red-600 transition"
          >
            <span class="text-lg font-semibold">Realizar Venta</span>
            <span class="material-icons text-3xl">arrow_forward</span>
          </router-link>
        </div>
      </section>
    </div>
  </template>
  
  <script>
  export default {
    name: "HomePage",
  };
  </script>
  
  <style scoped>
  /* Puedes personalizar estilos locales si es necesario */
  </style>
  