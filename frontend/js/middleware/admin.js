import store from '@/store'

export default (to, from, next) => {
  if (store.getters['auth/checkAdmin']) {
    next()
  } else {
    next({ name: 'protected' })
  }
}
