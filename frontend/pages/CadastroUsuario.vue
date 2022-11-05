<template>
    <div class="center" align="center">
        <v-card
            elevation="10"
            color="#F6E2E2"
            outlined
            width="600"
            height="650"
        ><h1 style="color:#000">Doe-se é melhor com você!</h1>
        <div class="center" align="center">
          <v-card
            elevation="0"
            color="#c6535f"
            outlined
            width="400"
          ><h2>Cadastro</h2>
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
              >
              </v-text-field>
              <v-text-field
                v-model="email"
                :rules="emailRules"
                label="E-mail"
                required
              ></v-text-field>
              <v-text-field
                v-model="cpf"
                :rules="cpfRules"
                label="CPF"
                required
              ></v-text-field>
              <v-text-field
                v-model="celular"
                :rules="celularRules"
                label="Telefone celular"
                required
              ></v-text-field>
              <v-text-field
                v-model="senha"
                :rules="senhaRules"
                label="Digite sua senha"
                type="password"
                required
              ></v-text-field>
              <v-text-field
                v-model="confirma"
                :rules="confirmaRules"
                label="Confirme sua senha"
                type="password"
                required
              ></v-text-field>
              <v-text-field
                v-model="dataNasc"
                :rules="dataNascRules"
                label="Data de nascimento"
                type="date"
              ></v-text-field>
              <div align="right"><v-btn
                :disabled="!valid"
                color="black"
                class="mr-4"
                @click="validate"
              >
                Pronto
              </v-btn></div>
            </v-form>
          </v-card>
        </div>

        </v-card>
    </div>
</template>
<script>

export default {
  name: 'CadastroUsuario',
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
        this.$router.push('./UserLogin')
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
