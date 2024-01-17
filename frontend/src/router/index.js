import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import AdView from '../views/AdView.vue'
import ManageBooksView from '../views/ManageBooksView.vue'
import BarUserView from '../views/BarUserView.vue'
import SearchTableView from '../views/SearchTableView.vue'
import UserView from '../views/UserView.vue'
import { getAuthToken } from '../api/apiClient'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      component: AboutView
    },
    {
      path: '/ads',
      name: 'ads',
      component: AdView
    },
    {
      path: '/manageBooks',
      name: 'manageBooks',
      component: ManageBooksView,
      beforeEnter: (to, from) => {
        const token = getAuthToken();
        console.log(token);
        return token != null;
      },
    },
    {
      path: '/barUser',
      name: 'barUser',
      component: BarUserView
    },
    {
      path: '/mainSearch',
      name: 'mainSearch',
      component: SearchTableView
    },
    {
      path: '/user',
      name: 'user',
      component: UserView
    }
  ]
})

export default router
