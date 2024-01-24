import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'

import Home from './components/Home.vue';
import About from './components/About.vue';
import Contact from './components/Contact.vue';
import User from './components/User.vue';
import App from './App.vue'

const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: '/',  name: 'home', component: Home },
        { path: '/about', name: 'about', component: About},
        { path: '/contact', name: 'contact' ,component: Contact },
        { path: '/user/:name', name: 'user' ,component: User },
    ]
});

const app = createApp(App)
app.use(router);
app.mount('#app')