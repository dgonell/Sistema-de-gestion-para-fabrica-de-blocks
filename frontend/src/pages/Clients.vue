<template>
  <div class="p-8 bg-gray-50 min-h-screen">
    <!-- Título -->
    <header class="mb-6">
      <h1 class="text-3xl font-bold text-gray-800">Registro de Clientes</h1>
      <p class="text-gray-600 mt-2">Agrega un nuevo cliente al sistema.</p>
    </header>

    <!-- Formulario -->
    <form @submit.prevent="validateAndRegister" class="bg-white shadow-lg rounded-lg p-6 max-w-2xl mx-auto">
      <div class="grid grid-cols-1 gap-6">
        <!-- Nombre -->
        <div>
          <label for="nombre" class="block text-sm font-medium text-gray-700">Nombre</label>
          <input
            type="text"
            id="nombre"
            v-model="client.nombre"
            @input="validateField('nombre')"
            class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
            :class="errors.nombre ? 'border-red-500' : ''"
            placeholder="Juan Pérez"
            maxlength="255"
            required
          />
          <p v-if="errors.nombre" class="text-red-500 text-sm mt-1">{{ errors.nombre }}</p>
        </div>

        <!-- Cédula/RNC -->
        <div>
          <label for="cedula" class="block text-sm font-medium text-gray-700">Cédula/RNC</label>
          <input
            type="text"
            id="cedula"
            v-model="client.cedula_rnc"
            @input="validateField('cedula_rnc')"
            class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
            :class="errors.cedula_rnc ? 'border-red-500' : ''"
            placeholder="12345678901"
            maxlength="13"
            required
          />
          <p v-if="errors.cedula_rnc" class="text-red-500 text-sm mt-1">{{ errors.cedula_rnc }}</p>
        </div>

        <!-- Teléfono -->
        <div>
          <label for="telefono" class="block text-sm font-medium text-gray-700">Teléfono</label>
          <input
            type="text"
            id="telefono"
            v-model="client.telefono"
            @input="validateField('telefono')"
            class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
            :class="errors.telefono ? 'border-red-500' : ''"
            placeholder="809-123-4567"
            maxlength="15"
            required
          />
          <p v-if="errors.telefono" class="text-red-500 text-sm mt-1">{{ errors.telefono }}</p>
        </div>

        <!-- Dirección -->
        <div>
          <label for="direccion" class="block text-sm font-medium text-gray-700">Dirección</label>
          <input
            type="text"
            id="direccion"
            v-model="client.direccion"
            @input="validateField('direccion')"
            class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
            :class="errors.direccion ? 'border-red-500' : ''"
            placeholder="Calle Principal #10"
            maxlength="255"
          />
          <p v-if="errors.direccion" class="text-red-500 text-sm mt-1">{{ errors.direccion }}</p>
        </div>
      </div>

      <!-- Botón -->
      <div class="mt-6">
        <button
          type="submit"
          class="w-full bg-blue-500 text-white py-2 px-4 rounded-md shadow-md hover:bg-blue-600 transition"
        >
          Registrar Cliente
        </button>
      </div>
    </form>

    <!-- Mensajes -->
    <div v-if="message" class="fixed bottom-4 right-4 bg-green-500 text-white py-2 px-4 rounded-md shadow-lg">
      {{ message }}
    </div>
    <div v-if="errorMessage" class="fixed bottom-4 right-4 bg-red-500 text-white py-2 px-4 rounded-md shadow-lg">
      {{ errorMessage }}
    </div>
  </div>
</template>

<script>
import api from "../services/api";

export default {
  name: "ClientsPage",
  data() {
    return {
      client: {
        nombre: "",
        cedula_rnc: "",
        telefono: "",
        direccion: "",
      },
      errors: {},
      message: null,
      errorMessage: null,
    };
  },
  methods: {
    validateField(field) {
      const value = this.client[field];
      switch (field) {
        case "nombre":
          if (!value) {
            this.errors.nombre = "El nombre es obligatorio.";
          } else if (value.length > 255) {
            this.errors.nombre = "El nombre no puede exceder 255 caracteres.";
          } else {
            delete this.errors.nombre;
          }
          break;
        case "cedula_rnc":
          if (!value) {
            this.errors.cedula_rnc = "La cédula o RNC es obligatoria.";
          } else if (value.length > 13) {
            this.errors.cedula_rnc = "La cédula o RNC no puede exceder 13 caracteres.";
          } else {
            delete this.errors.cedula_rnc;
          }
          break;
        case "telefono":
          if (!value) {
            this.errors.telefono = "El teléfono es obligatorio.";
          } else if (value.length > 15) {
            this.errors.telefono = "El teléfono no puede exceder 15 caracteres.";
          } else if (!/^\d{3}-\d{3}-\d{4}$/.test(value)) {
            this.errors.telefono = "El formato del teléfono debe ser 809-123-4567.";
          } else {
            delete this.errors.telefono;
          }
          break;
        case "direccion":
          if (value && value.length > 255) {
            this.errors.direccion = "La dirección no puede exceder 255 caracteres.";
          } else {
            delete this.errors.direccion;
          }
          break;
      }
    },
    validateAndRegister() {
      this.errors = {};
      Object.keys(this.client).forEach(this.validateField);
      if (Object.keys(this.errors).length === 0) {
        this.registerClient();
      } else {
        this.errorMessage = "Por favor corrige los errores antes de continuar.";
        setTimeout(() => {
          this.errorMessage = null;
        }, 3000);
      }
    },
    async registerClient() {
      try {
        await api.post("/clientes", this.client);
        this.message = "Cliente registrado exitosamente.";
        this.clearForm();

        setTimeout(() => {
          this.message = null;
        }, 3000);
      } catch (error) {
        console.error("Error al registrar el cliente:", error);
        this.errorMessage = "Ocurrió un error al registrar el cliente.";

        setTimeout(() => {
          this.errorMessage = null;
        }, 3000);
      }
    },
    clearForm() {
      this.client = {
        nombre: "",
        cedula_rnc: "",
        telefono: "",
        direccion: "",
      };
    },
  },
};
</script>

<style scoped>
/* Agrega estilos si es necesario */
</style>
