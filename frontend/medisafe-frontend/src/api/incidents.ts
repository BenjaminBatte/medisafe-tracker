import axios from "axios";

const API_URL = "http://127.0.0.1:5000/api/v1/incidents";

export interface Incident {
  id?: number;
  title: string;
  description: string;
  severity: string;
  user_id: number;
}

export const getIncidents = async (page = 1, per_page = 10) => {
  return axios.get(`${API_URL}/?page=${page}&per_page=${per_page}`);
};
