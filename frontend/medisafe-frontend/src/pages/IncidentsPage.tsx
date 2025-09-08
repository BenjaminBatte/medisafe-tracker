
import axios from "axios";

const API_BASE = "http://127.0.0.1:5000/api/v1/incidents"; // backend base URL

export interface Incident {
  id?: number;
  title: string;
  description: string;
  severity: "Low" | "Medium" | "High" | "Critical";
  user_id: number;
}

// Fetch incidents with pagination
export const getIncidents = (page = 1, per_page = 10) => {
  return axios.get(`${API_BASE}/`, {
    params: { page, per_page },
  });
};

// Create a new incident
export const addIncident = (incident: Incident) => {
  return axios.post(`${API_BASE}/`, incident);
};

// Fetch a single incident by ID
export const getIncidentById = (id: number) => {
  return axios.get(`${API_BASE}/${id}`);
};

// Update an incident
export const updateIncident = (id: number, incident: Partial<Incident>) => {
  return axios.put(`${API_BASE}/${id}`, incident);
};

// Delete an incident
export const deleteIncident = (id: number) => {
  return axios.delete(`${API_BASE}/${id}`);
};
