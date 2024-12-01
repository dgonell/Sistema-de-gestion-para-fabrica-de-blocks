<template>
    <div class="p-8 bg-gray-50">
      <header class="mb-6">
        <h1 class="text-3xl font-bold text-gray-800">Administrar Producción</h1>
        <p class="text-gray-600 mt-2">Gestiona los registros de producción existentes.</p>
      </header>
  
      <!-- Filtros -->
      <div class="mb-6 bg-white shadow-lg rounded-lg p-6">
        <h2 class="text-lg font-semibold mb-4">Filtrar Producción</h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
          <!-- Filtro por Fecha de Inicio -->
          <div>
            <label for="fecha_inicio" class="block text-sm font-medium text-gray-700">Fecha de Inicio</label>
            <input
              type="date"
              id="fecha_inicio"
              v-model="filters.fecha_inicio"
              @change="applyFilters"
              class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
            />
          </div>
  
          <!-- Filtro por Fecha de Fin -->
          <div>
            <label for="fecha_fin" class="block text-sm font-medium text-gray-700">Fecha de Fin</label>
            <input
              type="date"
              id="fecha_fin"
              v-model="filters.fecha_fin"
              @change="applyFilters"
              class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
            />
          </div>
  
          <!-- Filtro por Blocks -->
          <div>
            <label for="blocks" class="block text-sm font-medium text-gray-700">Cantidad de Blocks</label>
            <input
              type="number"
              id="blocks"
              v-model="filters.blocks"
              @input="applyFilters"
              class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
              placeholder="Ejemplo: 1000"
            />
          </div>
        </div>
      </div>
  
      <!-- Botón para abrir modal de impresión -->
      <div class="mb-4 flex justify-end">
        <button
          @click="openPrintModal"
          class="bg-green-500 text-white px-4 py-2 rounded shadow-md hover:bg-green-600 flex items-center space-x-2"
        >
          <span class="material-icons">print</span>
          <span>Imprimir</span>
        </button>
      </div>
  
      <!-- Tabla de Producción -->
      <div class="bg-white shadow-lg rounded-lg p-6">
        <div class="overflow-y-auto max-h-96">
          <table class="min-w-full border border-gray-200 text-left">
            <thead class="bg-gray-100">
              <tr>
                <th class="p-3 border border-gray-300">Fecha Inicio</th>
                <th class="p-3 border border-gray-300">Fecha Fin</th>
                <th class="p-3 border border-gray-300">Paletas</th>
                <th class="p-3 border border-gray-300">Blocks</th>
                <th class="p-3 border border-gray-300">Costo Total</th>
                <th class="p-3 border border-gray-300">Acciones</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="prod in filteredProduccion" :key="prod.id" class="hover:bg-gray-50">
                <td class="p-3 border border-gray-300">{{ prod.fecha_inicio }}</td>
                <td class="p-3 border border-gray-300">{{ prod.fecha_fin }}</td>
                <td class="p-3 border border-gray-300">{{ prod.paletas }}</td>
                <td class="p-3 border border-gray-300">{{ prod.blocks }}</td>
                <td class="p-3 border border-gray-300">{{ prod.costo_total }}</td>
                <td class="p-3 border border-gray-300 flex space-x-2">
                  <button @click="editProduction(prod)" class="text-blue-500 flex items-center">
                    <span class="material-icons">edit</span>
                  </button>
                  <button @click="deleteProduction(prod.id)" class="text-red-500 flex items-center">
                    <span class="material-icons">delete</span>
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
  
      <!-- Modal de Impresión -->
      <div v-if="printModalVisible" class="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center">
        <div class="bg-white p-6 rounded shadow-lg max-w-lg w-full">
          <h2 class="text-lg font-semibold mb-4">Imprimir Producción</h2>
  
          <!-- Selección de producciones -->
          <div class="max-h-64 overflow-y-auto">
            <ul>
              <li v-for="prod in filteredProduccion" :key="prod.id" class="flex items-center space-x-2 border-b py-2">
                <input type="checkbox" :value="prod.id" v-model="selectedProductionIds" class="form-checkbox" />
                <span>{{ prod.fecha_inicio }} - {{ prod.blocks }} blocks</span>
              </li>
            </ul>
          </div>
  
          <!-- Botones -->
          <div class="flex justify-end space-x-4 mt-4">
            <button
              @click="printSelectedProductions"
              class="bg-green-500 text-white px-4 py-2 rounded shadow-md hover:bg-green-600"
            >
              Imprimir Seleccionados
            </button>
            <button
              @click="closePrintModal"
              class="bg-gray-500 text-white px-4 py-2 rounded shadow-md hover:bg-gray-600"
            >
              Cancelar
            </button>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import api from "../services/api";
  
  export default {
    data() {
      return {
        produccion: [],
        filters: {
          fecha_inicio: "",
          fecha_fin: "",
          blocks: "",
        },
        filteredProduccion: [],
        printModalVisible: false,
        selectedProductionIds: [],
      };
    },
    methods: {
      async fetchProduccion() {
        try {
          const response = await api.get("/produccion");
          this.produccion = response.data;
          this.filteredProduccion = this.produccion; // Inicializa la lista filtrada
        } catch (error) {
          console.error("Error al cargar la producción:", error);
        }
      },
      applyFilters() {
        this.filteredProduccion = this.produccion.filter((prod) => {
          const matchesFechaInicio =
            !this.filters.fecha_inicio || prod.fecha_inicio >= this.filters.fecha_inicio;
          const matchesFechaFin =
            !this.filters.fecha_fin || prod.fecha_fin <= this.filters.fecha_fin;
          const matchesBlocks =
            !this.filters.blocks || prod.blocks >= parseInt(this.filters.blocks, 10);
  
          return matchesFechaInicio && matchesFechaFin && matchesBlocks;
        });
      },
      openPrintModal() {
        this.printModalVisible = true;
      },
      closePrintModal() {
        this.printModalVisible = false;
        this.selectedProductionIds = [];
      },
      printSelectedProductions() {
        const selectedProductions = this.produccion.filter((prod) =>
          this.selectedProductionIds.includes(prod.id)
        );
        console.log("Producciones seleccionadas para imprimir:", selectedProductions);
        alert("Producciones seleccionadas enviadas a impresión.");
        this.closePrintModal();
      },
      async deleteProduction(id) {
        if (confirm("¿Estás seguro de que deseas eliminar este registro de producción?")) {
          try {
            await api.delete(`/produccion/${id}`);
            this.fetchProduccion();
          } catch (error) {
            console.error("Error al eliminar la producción:", error);
          }
        }
      },
      editProduction(prod) {
        console.log("Editar producción:", prod);
        // Implementa la lógica de edición aquí
      },
    },
    mounted() {
      this.fetchProduccion();
    },
  };
  </script>
  
  <style>
  .material-icons {
    font-size: 24px;
  }
  </style>
  