<template>
  <b-container class="mt-4">
    <b-row>
      <b-col>
        <b-alert v-if="!operadoras.length" variant="info" show>
          Nenhuma operadora encontrada.
        </b-alert>

        <b-list-group v-else>
          <b-list-group-item
            v-for="operadora in operadoras"
            :key="operadora.id_operadora"
            class="d-flex flex-column"
          >
            <h5 class="text-primary mb-1">{{ operadora.nome_fantasia }}</h5>
            <small class="text-muted">CNPJ: {{ operadora.cnpj }}</small>
            <small>{{ operadora.razao_social }}</small>
          </b-list-group-item>
        </b-list-group>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
export default {
  props: {
    operadoras: {
      type: Array,
      required: true,
      default: () => [], 
    },
  },
};
</script>

<style scoped>
</style>
