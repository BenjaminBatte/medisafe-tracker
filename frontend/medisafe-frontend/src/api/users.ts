import axios from "axios";

export interface User {
  id?: number;
  first_name: string;
  last_name: string;
  email: string;
}

// Fetch users with pagination
export const getUsers = (page = 1, perPage = 10) =>
  axios.get(`http://127.0.0.1:5000/api/v1/users/`, {
    params: { page, per_page: perPage },
  });

// Add a new user
export const addUser = (user: User) =>
  axios.post(`http://127.0.0.1:5000/api/v1/users/`, user);
