import axios from 'axios'
import store from '@/store'
import router from '@/router'
import Cookies from 'js-cookie'
import NProgress from 'nprogress'
import swal from 'sweetalert2/dist/sweetalert2'
import i18n from './i18n'

axios.interceptors.request.use((request) => {
  NProgress.start()
  request.headers.common['X-CSRFToken'] = Cookies.get('csrftoken')

  const locale = store.getters['lang/locale']

  if (locale) {
    request.headers.common['Accept-Language'] = locale
  }

  request.baseURL = '/api/v1'
  return request
})

axios.interceptors.response.use(
  (response) => {
    NProgress.done()
    return response
  },
  (error) => {
    const status = error.response ? error.response.status : error.response
    NProgress.done()

    if (status >= 500) {
      swal.fire({
        icon: 'error',
        title: i18n.t('error_alert_title'),
        text: i18n.t('error_alert_text'),
        reverseButtons: true,
        confirmButtonText: i18n.t('ok'),
        cancelButtonText: i18n.t('cancel')
      })
    }

    if (status === 404) {
      router.push({ name: '404' })
    }

    if (status === 401 && store.getters['auth/check']) {
      return store
        .dispatch('auth/refresh')
        .then(() => {
          // error.config.baseURL = undefined;
          return axios.request(error.config)
        })
        .catch(() => {
          swal
            .fire({
              type: 'warning',
              title: i18n.t('token_expired_alert_title'),
              text: i18n.t('token_expired_alert_text'),
              reverseButtons: true,
              confirmButtonText: i18n.t('ok'),
              cancelButtonText: i18n.t('cancel')
            })
            .then(() => {
              store.commit('auth/LOGOUT')
              router.push({ name: 'login' })
            })
        })
    }

    return Promise.reject(error)
  }
)
