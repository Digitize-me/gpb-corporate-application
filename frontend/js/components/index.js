import Vue from 'vue'
import Child from './layout/Child'
import Example from './ui/Example'
;[
  Child,
  {
    name: 'example',
    ...Example
  }
  // if not component name
  // { name: 'component-name', ...Component }
].forEach(Component => {
  if (!Component.name) {
    throw new Error(`Not component name: ${Component}`)
  }

  Vue.component(Component.name, Component)
})
