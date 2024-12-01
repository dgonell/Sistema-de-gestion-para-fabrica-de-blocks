import { createRouter, createWebHistory } from "vue-router";
import Home from "../pages/Home.vue";
import Clients from "../pages/Clients.vue";
import Production from "../pages/Production.vue";
import Storage from "../pages/Storage.vue";
import Sales from "../pages/Sales.vue";
import RegisterClient from "../pages/Clients.vue";
import AdminClientes from "../pages/AdminClientes.vue";
import RegisterProduction from "../pages/RegistroProduccion.vue";
import AdminProduccion from "../pages/AdminProduccion.vue";

const routes = [
  { path: "/", name: "Home", component: Home },
  { path: "/clientes", name: "Clients", component: Clients },
  { path: "/produccion", name: "Production", component: Production },
  { path: "/almacen", name: "Storage", component: Storage },
  { path: "/ventas", name: "Sales", component: Sales },
  { path: "/clientes/registro", component: RegisterClient },
  { path: "/clientes/administrar", component: AdminClientes },
  { path: "/produccion/registro", component: RegisterProduction },
  { path: "/produccion/administrar", component: AdminProduccion },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
