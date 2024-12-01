<template>
  <div id="app" class="min-h-screen flex bg-gray-50">
    <!-- Sidebar -->
    <aside class="w-64 bg-gray-800 text-white min-h-screen fixed">
      <div class="p-4 text-center border-b border-gray-700">
        <h1 class="text-xl font-bold">Sistema de Blocks</h1>
      </div>
      <nav class="mt-4">
        <ul class="space-y-2">
          <!-- Inicio -->
          <li>
            <router-link
              to="/"
              class="flex items-center px-4 py-2 hover:bg-gray-700 transition"
              :class="{ 'bg-gray-700': $route.path === '/' }"
            >
              <span class="material-icons mr-2">home</span>
              Inicio
            </router-link>
          </li>

          <!-- Clientes Dropdown -->
          <li class="group">
            <div
              class="flex items-center px-4 py-2 hover:bg-gray-700 transition cursor-pointer"
              @click="toggleDropdown('clientes')"
            >
              <span class="material-icons mr-2">people</span>
              Clientes
              <span class="material-icons ml-auto">
                {{ dropdowns.clientes ? 'expand_less' : 'expand_more' }}
              </span>
            </div>
            <ul
              v-if="dropdowns.clientes"
              class="ml-4 mt-2 space-y-2"
            >
              <li>
                <router-link
                  to="/clientes/registro"
                  class="block px-4 py-2 hover:bg-gray-700 transition"
                >
                  Registrar Cliente
                </router-link>
              </li>
              <li>
                <router-link
                  to="/clientes/administrar"
                  class="block px-4 py-2 hover:bg-gray-700 transition"
                >
                  Administrar Clientes
                </router-link>
              </li>
            </ul>
          </li>

          <!-- Producción -->
          <!-- Producción Dropdown -->
          <li class="group">
            <div
              class="flex items-center px-4 py-2 hover:bg-gray-700 transition cursor-pointer"
              @click="toggleDropdown('produccion')"
            >
              <span class="material-icons mr-2">factory</span>
              Producción
              <span class="material-icons ml-auto">
                {{ dropdowns.produccion ? 'expand_less' : 'expand_more' }}
              </span>
            </div>
            <ul
              v-if="dropdowns.produccion"
              class="ml-4 mt-2 space-y-2"
            >
              <li>
                <router-link
                  to="/produccion/registro"
                  class="block px-4 py-2 hover:bg-gray-700 transition"
                >
                  Registrar Producción
                </router-link>
              </li>
              <li>
                <router-link
                  to="/produccion/administrar"
                  class="block px-4 py-2 hover:bg-gray-700 transition"
                >
                  Administrar Producción
                </router-link>
              </li>
            </ul>
          </li>

          <!-- Almacén -->
          <li>
            <router-link
              to="/almacen"
              class="flex items-center px-4 py-2 hover:bg-gray-700 transition"
              :class="{ 'bg-gray-700': $route.path === '/almacen' }"
            >
              <span class="material-icons mr-2">inventory</span>
              Almacén
            </router-link>
          </li>

          <!-- Ventas -->
          <li>
            <router-link
              to="/ventas"
              class="flex items-center px-4 py-2 hover:bg-gray-700 transition"
              :class="{ 'bg-gray-700': $route.path === '/ventas' }"
            >
              <span class="material-icons mr-2">shopping_cart</span>
              Ventas
            </router-link>
          </li>
        </ul>
      </nav>
    </aside>

    <!-- Main Content -->
    <div class="ml-64 flex-1">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      dropdowns: {
        clientes: false,
      },
    };
  },
  methods: {
    toggleDropdown(menu) {
      this.dropdowns[menu] = !this.dropdowns[menu];
    },
  },
};
</script>

<style>
/* Estilo adicional si es necesario */
.material-icons {
  font-size: 20px;
}
</style>
