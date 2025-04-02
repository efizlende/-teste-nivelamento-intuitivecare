<template>
  <div class="container mt-5">
    <div class="row">
      <div class="col-12">
        <SearchBar @search="fetchOperadoras" />
      </div>
      <div class="col-12">
        <OperadoraList :operadoras="operadoras" />
      </div>
    </div>
  </div>
</template>

<script>
import SearchBar from "./components/searchBar.vue";
import OperadoraList from "./components/operadoraList.vue";
import { searchOperadoras } from "./api/operadoraService.js";

export default {
  name: "App",
  components: {
    SearchBar,
    OperadoraList,
  },
  data() {
    return {
      operadoras: [],
    };
  },
  methods: {
    async fetchOperadoras(query) {
      this.operadoras = await searchOperadoras(query);
    },
  },
};
</script>

