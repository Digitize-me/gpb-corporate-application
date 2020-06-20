<template>
  <v-row align="center" justify="center">
    <v-col cols="12" sm="8" md="4">
      <v-card class="elevation-12">
        <v-card-text>
          <v-form>
            <v-text-field
              id="inputLogin"
              type="text"
              v-model.trim="username"
              :placeholder="$t('user_name')"
            ></v-text-field>
            <v-text-field
              id="inputPass"
              type="password"
              v-model.trim="password"
              :placeholder="$t('password')"
            ></v-text-field>
          </v-form>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn @click="handleSubmit()">Login</v-btn>
        </v-card-actions>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
  export default {
    layout: 'empty',
    data() {
      return {
        username: '',
        password: ''
      }
    },
    methods: {
      handleSubmit(e) {
        const { username, password } = this
        const { dispatch } = this.$store
        if (username && password) {
          dispatch('auth/login', { username, password })
            .then(response => {
              const next = this.$route.query.next || '/'
              this.$router.push(next)
            })
            .catch(error => {
              console.log('ssd', error)
            })
        }
      }
    }
  }
</script>
