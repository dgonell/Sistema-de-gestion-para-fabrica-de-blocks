import { createApp } from 'vue';
import App from './App.vue';
import './main.css'; // Importa Tailwind CSS
import router from './router';

createApp(App).use(router).mount('#app');
