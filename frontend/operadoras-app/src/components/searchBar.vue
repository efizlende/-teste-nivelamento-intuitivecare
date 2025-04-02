<template>
  <div class="p-4 bg-primary text-white rounded-lg shadow-sm">
    <input
      v-model.trim="searchQuery" 
      type="text"
      placeholder="Buscar operadora..."
      class="form-control"
      @input="debouncedSearch"
    />
  </div>
</template>

<script>
import { ref } from "vue";
import { debounce } from "lodash"; 

export default {
  emits: ["search"],
  setup(_, { emit }) {
    const searchQuery = ref("");


    const debouncedSearch = debounce(() => {
      emit("search", searchQuery.value);
    }, 300); 

    return { searchQuery, debouncedSearch };
  },
};
</script>

<style scoped>
</style>
