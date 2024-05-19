import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import AdView from '../views/AdView.vue'
import ManageBooksView from '../views/ManageBooksView.vue'
import BarUserView from '../views/BarUserView.vue'
import SearchTableView from '../views/SearchTableView.vue'
import UserView from '../views/UserView.vue'
import HistoricalBooks from '../views/HistoricalBooks.vue'
import adminBares from '../views/adminBares.vue'
import { getAuthToken,getClaimsFromToken } from '../api/apiClient'


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
      component: AdView,
      beforeEnter: (to, from, next) => {
        const token = getAuthToken();

        if (token) {
          const userRole = getClaimsFromToken(token).role; // Ajusta esto según la estructura real de tus tokens

          if (userRole === 'bar') {
            next();
          } else {
            next({ name: 'home' });
          }
        } else {
          next({ name: 'home' });
        }
      },
    },
    {
      path: '/manageBooks',
      name: 'manageBooks',
      component: ManageBooksView,
      beforeEnter: (to, from, next) => {
        const token = getAuthToken();

        if (token) {
          const userRole = getClaimsFromToken(token).role; // Ajusta esto según la estructura real de tus tokens

          if (userRole === 'bar') {
            next();
          } else {
            next({ name: 'home' });
          }
        } else {
          next({ name: 'home' });
        }
      },
    },
    {
      path: '/barUser',
      name: 'barUser',
      component: BarUserView,
      beforeEnter: (to, from, next) => {
        const token = getAuthToken();

        if (token) {
          const userRole = getClaimsFromToken(token).role; // Ajusta esto según la estructura real de tus tokens

          if (userRole === 'bar') {
            next();
          } else {
            next({ name: 'home' });
          }
        } else {
          next({ name: 'home' });
        }
      },
    },
    {
      path: '/mainSearch',
      name: 'mainSearch',
      component: SearchTableView,
      beforeEnter: (to, from, next) => {
        const token = getAuthToken();

        if (token) {
          const userRole = getClaimsFromToken(token).role; // Ajusta esto según la estructura real de tus tokens

          if (userRole === 'user') {
            next();
          } else {
            next({ name: 'home' });
          }
        } else {
          next({ name: 'home' });
        }
      },
    },
    {
      path: '/user',
      name: 'user',
      component: UserView,
      beforeEnter: (to, from, next) => {
        const token = getAuthToken();

        if (token) {
          const userRole = getClaimsFromToken(token).role; // Ajusta esto según la estructura real de tus tokens

          if (userRole === 'user') {
            next();
          } else {
            next({ name: 'home' });
          }
        } else {
          next({ name: 'home' });
        }
      },
    },
    {
      path: '/histbooks',
      name: 'histbooks',
      component: HistoricalBooks,
      beforeEnter: (to, from, next) => {
        const token = getAuthToken();

        if (token) {
          const userRole = getClaimsFromToken(token).role; // Ajusta esto según la estructura real de tus tokens

          if (userRole === 'admin') {
            next();
          } else {
            next({ name: 'home' });
          }
        } else {
          next({ name: 'home' });
        }
      },
    },
    {
      path: '/all_bars',
      name: 'all_bars',
      component: adminBares,
      beforeEnter: (to, from, next) => {
        const token = getAuthToken();

        if (token) {
          const userRole = getClaimsFromToken(token).role; // Ajusta esto según la estructura real de tus tokens

          if (userRole === 'admin') {
            next();
          } else {
            next({ name: 'home' });
          }
        } else {
          next({ name: 'home' });
        }
      },
    },
  ]
})

export default router
