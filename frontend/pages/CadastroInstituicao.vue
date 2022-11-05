<template>
    <div class="center" align="center">
        <v-card
            elevation="10"
            color="#F6E2E2"
            outlined
            width="1400"
            height="650"
        >
            <v-form
                v-model="valid"
                ref="formInst"
                lazy-validation
            ><v-row>
                    <v-col>
                        <v-text-field
                            v-model="cnpj"
                            :counter="14"
                            :rules="cnpjRules"
                            label="CNPJ próprio/mantedouro"
                            required>
                        ></v-text-field>
                    </v-col>
                    <v-col>
                        <v-text-field
                            v-model="nomeRepresentante"
                            :rules="nomeRepresentanteRules"
                            label="Nome do representante"
                            required>
                        ></v-text-field>
                    </v-col>
                    <v-col>
                        <v-select
                            v-model="tipoInst"
                            :items="tiposInst"
                            :rules="[v => !!v || 'Selecione o tipo']"
                            label="Tipo"
                            required
                            ></v-select>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col>
                        <v-text-field
                            v-model="rua"
                            :rules="ruaRules"
                            label="Rua"
                            required>
                        ></v-text-field>
                    </v-col>
                    <v-col cols="1">
                        <v-text-field
                            v-model="numero"
                            :rules="numeroRules"
                            label="numero"
                            required>
                        ></v-text-field>
                    </v-col>
                    <v-col>
                        <v-text-field
                            v-model="bairro"
                            :rules="bairroRules"
                            label="Bairro"
                            required>
                        ></v-text-field>
                    </v-col>
                </v-row>
                <v-row>
                <v-col>
                    <v-text-field
                        v-model="cidade"
                        :rules="cidadeRules"
                        label="Cidade"
                        required>
                    ></v-text-field>
                    </v-col>
                    <v-col cols="1">
                        <v-select
                            v-model="uf"
                            :items="ufs"
                            :rules="[v => !!v || 'Selecione a UF']"
                            label="UF"
                            required
                        ></v-select>
                    </v-col>
                    <v-col>
                        <v-text-field
                            v-model="cep"
                            :rules="cepRules"
                            label="CEP"
                            required>
                        ></v-text-field>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col>
                    <v-select
                        v-model="subTipo"
                        :items="subTipos"
                        :rules="[v => !!v || 'Selecione o subtipo']"
                        label="Subtip"
                        required
                        ></v-select>
                    </v-col>
                    <v-col>
                        <v-text-field
                            v-model="nomeInst"
                            :rules="nomeInstRules"
                            label="Nome institucional"
                            required>
                        ></v-text-field>
                    </v-col>
                    <v-col>
                        <v-text-field
                            v-model="nomeFantasia"
                            :rules="nomeFantasiaRules"
                            label="Nome fatasia"
                            required>
                        ></v-text-field>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col>
                        <v-text-field
                            v-model="telefoneRep"
                            :rules="telefoneRepRules"
                            label="Telefone do Representante"
                            required>
                        ></v-text-field>
                    </v-col>
                    <v-col>
                        <v-text-field
                            v-model="emailInst"
                            :rules="emailInstRules"
                            label="e-mail institucional"
                            required>
                        ></v-text-field>
                    </v-col>
                    <v-col>
                        <v-text-field
                            v-model="emailRep"
                            :rules="emailRepRules"
                            label="e-mail do Representante"
                            required>
                        ></v-text-field>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col cols="4">
                        <v-text-field
                            v-model="senhaInst"
                            :rules="senhaInstRules"
                            label="Senha"
                            type="password"
                            required>
                        ></v-text-field>
                    </v-col>
                    <v-col cols="4">
                        <v-text-field
                            v-model="confirmaInst"
                            :rules="confirmaInstRules"
                            label="Confirmação"
                            type="password"
                            required>
                        ></v-text-field>
                    </v-col>
                </v-row>
                <div align="right"><v-btn
                    :disabled="!valid"
                    color="black"
                    class="mr-4"
                    @click="validate"
                >Cadastrar</v-btn></div>
            </v-form>
        </v-card>
    </div>
</template>
<script>
export default {
  name: 'CadastroInstituicao',
  layout: 'navbar',
  data: () => ({
    valid: true,
    cnpj: '',
    cnpjRules: [
      v => !!v || 'CNPJ obrigatório',
      v => (!/[^0-9]/.test(v) && v.length === 14) || 'CNPJ invalido'
    ],
    nomeRepresentante: '',
    nomeRepresentanteRules: [
      v => !!v || 'Nome obrigatório',
      v => (!/[^a-zA-Z\s]+/.test(v) && !/\s\s/.test(v) && v[0] !== ' ') || 'Nome invalido'
    ],
    tipoInst: null,
    tiposInst: [
      'ONG',
      'Instituição religiosa',
      'Instituição filantrópica'
    ],
    rua: '',
    ruaRules: [
      v => !!v || 'Rua obrigatória'
    ],
    numero: '',
    numeroRules: [
      v => !!v || 'Numero obragatório',
      v => (!/[^0-9]/.test(v) && v.length <= 5 && v > 0) || 'numero invalido'
    ],
    bairro: '',
    bairroRules: [
      v => !!v || 'Bairro obrigatório'
    ],
    cidade: '',
    cidadeRules: [
      v => !!v || 'Cidade obrigatória'
    ],
    uf: null,
    ufs: [
      'SP',
      'RJ',
      'MG',
      'ES'
    ],
    cep: '',
    cepRules: [
      v => !!v || 'CEP obrigatório',
      v => (!/[^0-9]/.test(v) && v.length === 8) || 'CEP invalido'
    ],
    subTipo: 'n/a',
    subTipos: [
      'n/a'
    ],
    nomeInst: '',
    nomeInstRules: [
      v => !!v || 'Nome obirgatório'
    ],
    nomeFantasia: '',
    telefoneRep: '',
    telefoneRepRules: [
      v => !!v || 'Telefone obrigatório',
      v => ((/(11|12|21)[0-9]{8}/.test(v) && v.length === 10) || (/(11|12|21)9[0-9]{8}/.test(v) && v.length === 11)) || 'Telefone invalido'
    ],
    emailInst: '',
    emailInstRules: [
      v => !!v || 'e-mail obrigatório',
      v => /.+@.+\..+/.test(v) || 'e-mail invalido'
    ],
    emailRep: '',
    emailRepRules: [
      v => !!v || 'e-mail obrigatório',
      v => /.+@.+\..+/.test(v) || 'e-mail invalido'
    ],
    senhaInst: '',
    senhaInstRules: [
      v => !!v || 'senha obrigatória',
      v => v.length >= 8 || 'Menos de 8 caracteres'
    ],
    confirmaInst: '',
    confirmaInstRules: [
      v => !!v || 'senha obrigatória',
      v => v.length >= 8 || 'Menos de 8 caracteres'
      // v => v === this.senhaInst || 'Senhas não batem'
    ]
  }),
  methods: {
    validate () {
      if (this.$refs.formInst.validate()) {
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
