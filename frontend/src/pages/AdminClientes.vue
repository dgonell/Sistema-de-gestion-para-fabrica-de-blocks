<template>
    <div class="p-8 bg-gray-50">
      <!-- Título -->
      <header class="mb-6">
        <h1 class="text-3xl font-bold text-gray-800">Administrar Clientes</h1>
        <p class="text-gray-600 mt-2">Gestiona los clientes registrados en el sistema.</p>
      </header>
  
      <!-- Filtros -->
      <div class="mb-6 bg-white shadow-lg rounded-lg p-6">
        <h2 class="text-lg font-semibold mb-4">Filtrar Clientes</h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
          <!-- Filtro por Nombre -->
          <div>
            <label for="nombre" class="block text-sm font-medium text-gray-700">Nombre</label>
            <input
              type="text"
              id="nombre"
              v-model="filters.nombre"
              @input="applyFilters"
              class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
              placeholder="Ejemplo: Juan Pérez"
            />
          </div>
  
          <!-- Filtro por Cédula/RNC -->
          <div>
            <label for="cedula" class="block text-sm font-medium text-gray-700">Cédula/RNC</label>
            <input
              type="text"
              id="cedula"
              v-model="filters.cedula_rnc"
              @input="applyFilters"
              class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
              placeholder="Ejemplo: 12345678901"
            />
          </div>
  
          <!-- Filtro por Fecha -->
          <div>
            <label for="fecha" class="block text-sm font-medium text-gray-700">Fecha de Registro</label>
            <div class="flex space-x-2 mt-1">
              <input
                type="date"
                v-model="filters.startDate"
                @change="applyFilters"
                class="block w-1/2 rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
              />
              <input
                type="date"
                v-model="filters.endDate"
                @change="applyFilters"
                class="block w-1/2 rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
              />
            </div>
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
  
      <!-- Tabla de Clientes -->
      <div class="bg-white shadow-lg rounded-lg p-6">
        <div class="overflow-y-auto max-h-96">
          <table class="min-w-full border border-gray-200 text-left">
            <thead class="bg-gray-100">
              <tr>
                <th class="p-3 border border-gray-300">Nombre</th>
                <th class="p-3 border border-gray-300">Cédula/RNC</th>
                <th class="p-3 border border-gray-300">Teléfono</th>
                <th class="p-3 border border-gray-300">Dirección</th>
                <th class="p-3 border border-gray-300">Acciones</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="cliente in filteredClientes" :key="cliente.id" class="hover:bg-gray-50">
                <td class="p-3 border border-gray-300">{{ cliente.nombre }}</td>
                <td class="p-3 border border-gray-300">{{ cliente.cedula_rnc }}</td>
                <td class="p-3 border border-gray-300">{{ cliente.telefono }}</td>
                <td class="p-3 border border-gray-300">{{ cliente.direccion }}</td>
                <td class="p-3 border border-gray-300 flex space-x-2">
                  <button @click="editCliente(cliente)" class="text-blue-500 flex items-center">
                    <span class="material-icons">edit</span>
                  </button>
                  <button @click="deleteCliente(cliente.id)" class="text-red-500 flex items-center">
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
          <h2 class="text-lg font-semibold mb-4">Imprimir Clientes</h2>
          <div class="max-h-64 overflow-y-auto">
            <ul>
              <li v-for="cliente in filteredClientes" :key="cliente.id" class="flex items-center space-x-2 border-b py-2">
                <input type="checkbox" :value="cliente.id" v-model="selectedClientIds" class="form-checkbox" />
                <span>{{ cliente.nombre }}</span>
              </li>
            </ul>
          </div>
          <div class="flex justify-end space-x-4 mt-4">
            <button @click="printSelectedClients" class="bg-green-500 text-white px-4 py-2 rounded shadow-md hover:bg-green-600">
              Imprimir Seleccionados
            </button>
            <button @click="printByDateRange" class="bg-blue-500 text-white px-4 py-2 rounded shadow-md hover:bg-blue-600">
              Imprimir por Fecha
            </button>
            <button @click="closePrintModal" class="bg-gray-500 text-white px-4 py-2 rounded shadow-md hover:bg-gray-600">
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
        clientes: [],
        filteredClientes: [],
        filters: {
          nombre: "",
          cedula_rnc: "",
          startDate: "",
          endDate: "",
        },
        selectedClientIds: [],
        printModalVisible: false,
      };
    },
    methods: {
      async fetchClientes() {
        try {
          const response = await api.get("/clientes");
          this.clientes = response.data;
          this.filteredClientes = this.clientes; // Inicializa la lista filtrada
        } catch (error) {
          console.error("Error al cargar los clientes:", error);
        }
      },
      applyFilters() {
        this.filteredClientes = this.clientes.filter((cliente) => {
          const matchesNombre = cliente.nombre.toLowerCase().includes(this.filters.nombre.toLowerCase());
          const matchesCedula = cliente.cedula_rnc.includes(this.filters.cedula_rnc);
          let matchesFecha = true;
  
          if (this.filters.startDate && this.filters.endDate) {
            const createdAt = new Date(cliente.created_at);
            const start = new Date(this.filters.startDate);
            const end = new Date(this.filters.endDate);
            matchesFecha = createdAt >= start && createdAt <= end;
          }
  
          return matchesNombre && matchesCedula && matchesFecha;
        });
      },
      openPrintModal() {
        this.printModalVisible = true;
      },
      closePrintModal() {
        this.printModalVisible = false;
        this.selectedClientIds = [];
      },
      printSelectedClients() {
        const selectedClients = this.clientes.filter((cliente) =>
          this.selectedClientIds.includes(cliente.id)
        );
        console.log("Clientes seleccionados para imprimir:", selectedClients);
        alert("Clientes seleccionados enviados a impresión.");
        this.closePrintModal();
      },
      printByDateRange() {
        const filteredClients = this.filteredClientes;
        console.log("Clientes filtrados para impresión:", filteredClients);
        alert("Clientes filtrados enviados a impresión.");
        this.closePrintModal();
      },
      editCliente(cliente) {
        console.log("Editar cliente:", cliente);
      },
      deleteCliente(id) {
        console.log("Eliminar cliente con ID:", id);
      },
    },
    mounted() {
      this.fetchClientes();
    },
  };
  </script>
  
  <style>
  .material-icons {
    font-size: 24px;
  }
  </style>
  