import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:5000",  
});





export const searchOperadoras = async (query) => {
  try {
    const response = await api.get(`/search`, { params: { query } });
    return response.data;
  } catch (error) {
    console.error("Erro ao buscar operadoras:", error);
    return [];
  }
};
