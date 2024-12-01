<template>
    <div class="p-8 bg-gray-50">
      <header class="mb-6">
        <h1 class="text-3xl font-bold text-gray-800">Registrar Producción</h1>
        <p class="text-gray-600 mt-2">Completa los detalles para agregar un nuevo registro de producción.</p>
      </header>
  
      <form @submit.prevent="registerProduction" class="bg-white shadow-lg rounded-lg p-6 max-w-2xl mx-auto">
        <div class="grid grid-cols-1 gap-6">
          <!-- Fecha Inicio -->
          <div>
            <label for="fecha_inicio" class="block text-sm font-medium text-gray-700">Fecha de Inicio</label>
            <input
              type="date"
              id="fecha_inicio"
              v-model="production.fecha_inicio"
              class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
              required
            />
          </div>
  
          <!-- Fecha Fin -->
          <div>
            <label for="fecha_fin" class="block text-sm font-medium text-gray-700">Fecha de Fin</label>
            <input
              type="date"
              id="fecha_fin"
              v-model="production.fecha_fin"
              class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
              required
            />
          </div>
  
          <!-- Paletas -->
          <div>
            <label for="paletas" class="block text-sm font-medium text-gray-700">Cantidad de Paletas</label>
            <input
              type="number"
              id="paletas"
              v-model.number="production.paletas"
              @input="calculateFields"
              class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
              placeholder="Ejemplo: 10"
              required
            />
          </div>
  
          <!-- Blocks (Calculado y Bloqueado) -->
          <div>
            <label for="blocks" class="block text-sm font-medium text-gray-700">Cantidad de Blocks</label>
            <input
              type="text"
              id="blocks"
              :value="formattedBlocks"
              disabled
              class="mt-1 block w-full rounded-md border-gray-300 bg-gray-100 shadow-sm focus:border-blue-500 focus:ring-blue-500"
            />
          </div>
  
          <!-- Costo Total (Calculado y Bloqueado) -->
          <div>
            <label for="costo_total" class="block text-sm font-medium text-gray-700">Costo Total</label>
            <input
              type="text"
              id="costo_total"
              :value="formattedCostoTotal"
              disabled
              class="mt-1 block w-full rounded-md border-gray-300 bg-gray-100 shadow-sm focus:border-blue-500 focus:ring-blue-500"
            />
          </div>
        </div>
  
        <!-- Botón -->
        <div class="mt-6">
          <button
            type="submit"
            class="w-full bg-blue-500 text-white py-2 px-4 rounded-md shadow-md hover:bg-blue-600 transition"
          >
            Registrar Producción
          </button>
        </div>
      </form>
    </div>
  </template>
  
  <script>
  import api from "../services/api";
  
  export default {
    data() {
      return {
        production: {
          fecha_inicio: "",
          fecha_fin: "",
          paletas: 0,
          blocks: 0,
          costo_total: 0,
        },
      };
    },
    computed: {
      formattedBlocks() {
        // Formatear la cantidad de blocks con guiones (e.g., 1-000-000)
        return new Intl.NumberFormat("es-ES").format(this.production.blocks);
      },
      formattedCostoTotal() {
        // Formatear el costo total como moneda
        return new Intl.NumberFormat("es-ES", {
          style: "currency",
          currency: "DOP",
        }).format(this.production.costo_total);
      },
    },
    methods: {
      calculateFields() {
        // Calcular la cantidad de blocks y el costo total automáticamente
        this.production.blocks = this.production.paletas * 138;
        this.production.costo_total = this.production.blocks * 3;
      },
      async registerProduction() {
        try {
          // Enviar los datos sin el formato aplicado (solo los valores reales)
          const payload = {
            fecha_inicio: this.production.fecha_inicio,
            fecha_fin: this.production.fecha_fin,
            paletas: this.production.paletas,
            blocks: this.production.blocks,
            costo_total: this.production.costo_total,
          };
  
          console.log("Datos enviados al backend:", payload);
          await api.post("/produccion", payload);
          alert("Producción registrada exitosamente.");
          this.clearForm();
        } catch (error) {
          console.error("Error al registrar la producción:", error.response.data);
          alert("No se pudo registrar la producción.");
        }
      },
      clearForm() {
        this.production = {
          fecha_inicio: "",
          fecha_fin: "",
          paletas: 0,
          blocks: 0,
          costo_total: 0,
        };
      },
    },
  };
  </script>
  