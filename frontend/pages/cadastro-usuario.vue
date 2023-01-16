<template>
    <div class="center" align="center">
        <v-card
            elevation="10"
            color="#F6E2E2"
            outlined
            width="30vw"
            height="80vh"
        >
        <div class="center" align="center">
        <h2>Cadastro</h2>
          <v-form
            ref="formUser"
            v-model="valid"
            lazy-validation
          >
            <v-text-field
            v-model="name"
            :counter="25"
            :rules="nameRules"
            label="Nome"
            required
            outlined
            filled
            background-color="#f6f6f6"
            style="width:25vw"
            >
            </v-text-field>
            <v-text-field
              v-model="email"
              :rules="emailRules"
              label="E-mail"
              required
              outlined
              filled
              background-color="#f6f6f6"
            ></v-text-field>
            <v-text-field
              v-model="cpf"
              :rules="cpfRules"
              label="CPF"
              required
              outlined
              filled
              background-color="#f6f6f6"
            ></v-text-field>
            <v-text-field
              v-model="celular"
              :rules="celularRules"
              label="Telefone celular"
              required
              outlined
              filled
              background-color="#f6f6f6"
            ></v-text-field>
            <v-text-field
              v-model="senha"
              :rules="senhaRules"
              label="Digite sua senha"
              type="password"
              required
              outlined
              filled
              background-color="#f6f6f6"
            ></v-text-field>
            <v-text-field
              v-model="confirma"
              :rules="confirmaRules"
              label="Confirme sua senha"
              type="password"
              required
              outlined
              filled
              background-color="#f6f6f6"
            ></v-text-field>
            <v-text-field
              v-model="dataNasc"
              :rules="dataNascRules"
              label="Data de nascimento"
              type="date"
            ></v-text-field>
            <div align="right"><v-btn
              :disabled="!valid"
              color="#d8d5d5"
              class="mr-4"
              @click="validate"
            >
              Pronto
            </v-btn></div>
            </v-form>
        </div>

        </v-card>
    </div>
</template>
<script>

export default {
  name: 'Cadastro-Usuario',
  layout: 'navbar',
  data: () => ({
    valid: true,
    name: '',
    nameRules: [
      v => !!v || 'Nome obrigatório',
      v => (v && v.length <= 25) || 'Maximo 25 caracteres'
    ],
    email: '',
    emailRules: [
      v => !!v || 'E-mail obrigatório',
      v => /.+@.+\..+/.test(v) || 'E-mail invalido'
    ],
    cpf: '',
    cpfRules: [
      v => !!v || 'CPF obrigatório',
      v => (!/[^0-9]/.test(v) && v.length === 11) || 'CPF invalido'
    ],
    celular: '',
    celularRules: [
      v => !!v || 'Celular obrigatarório',
      v => (/(12|11|21)9[0-9]{8}/.test(v) && v.length === 11) || 'Celular invalido'
    ],
    senha: '',
    senhaRules: [
      v => !!v || 'senha obrigatória',
      v => v.length >= 8 || 'Menos de 8 caracteres'
    ],
    confirma: '',
    confirmaRules: [
      v => !!v || 'senha obrigatória',
      v => v.length >= 8 || 'Menos de 8 caracteres'
    ]
  }),
  methods: {
    validate () {
      if (this.$refs.formUser.validate()) {
        this.$router.push('./login-usuario')
      }
    }
  }
}
</script>
<style>
.center {
  margin: 0;
  position: absolute;
  top: 50%;
  left: 50%;
  -ms-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
}
</style>
