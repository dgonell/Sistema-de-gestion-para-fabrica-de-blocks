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
      </div>
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
              <!-- Datos con máscara aplicada -->
              <td class="p-3 border border-gray-300">{{ prod.fecha_inicio }}</td>
              <td class="p-3 border border-gray-300">{{ prod.fecha_fin }}</td>
              <td class="p-3 border border-gray-300">{{ prod.paletas }}</td>
              <td class="p-3 border border-gray-300">{{ formatBlocks(prod.blocks) }}</td>
              <td class="p-3 border border-gray-300">{{ formatCostoTotal(prod.costo_total) }}</td>
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
  </div>
</template>

<script>
import api from "../services/api";

export default {
  name: "AdminProduction",
  data() {
    return {
      produccion: [],
      filters: {
        fecha_inicio: "",
        fecha_fin: "",
      },
      filteredProduccion: [],
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
        return matchesFechaInicio && matchesFechaFin;
      });
    },
    formatBlocks(blocks) {
      // Formatear blocks con separadores de miles
      return new Intl.NumberFormat("es-ES").format(blocks);
    },
    formatCostoTotal(costo) {
      // Formatear costo total como moneda
      return new Intl.NumberFormat("es-ES", {
        style: "currency",
        currency: "DOP",
      }).format(costo);
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
