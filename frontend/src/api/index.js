import axios from 'axios';

const API_BASE_URL = process.env.NODE_ENV === 'production' ? '' : 'http://localhost:8000';

const api = axios.create({
    baseURL: `${API_BASE_URL}/api`
});

const token = localStorage.getItem('token');

if (token) {
    api.defaults.headers.common['Authorization'] = `Token ${token}`;
}

export default api;
