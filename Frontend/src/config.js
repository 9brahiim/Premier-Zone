// API Configuration
// In production, this will be set via environment variable
// For local development, defaults to localhost:8000 (FastAPI default port)
const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

export default API_BASE_URL;

