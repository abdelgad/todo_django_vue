import { createWebHistory, createRouter } from "vue-router";
import Home from './views/Home';
import Login from './views/Login';
import Logout from './views/Logout';

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home,
    meta: {
      requiresLogin: true
    }
  },
  {
    path: '/login',
    name: 'login',
    component: Login,
  },
  {
    path: '/logout',
    name: 'logout',
    component: Logout,
  },
];

export default createRouter({
  history: createWebHistory(),
  routes,
});
