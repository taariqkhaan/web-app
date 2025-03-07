import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:8000";

// Fetch all projects
export const getProjects = async () => {
    const response = await axios.get(`${API_BASE_URL}/projects/`);
    return response.data;
};

// Fetch a single project by ID
export const getProjectById = async (id) => {
    const response = await axios.get(`${API_BASE_URL}/projects/${id}`);
    return response.data;
};

// Create a new project
export const createProject = async (projectData) => {
    const response = await axios.post(`${API_BASE_URL}/projects/`, projectData);
    return response.data;
};
