import store from '@/store'

export default (to, from, next) => {
  if (store.getters['auth/checkStaff']) {
    next()
  } else {
    next({ name: 'protected' })
  }
}
