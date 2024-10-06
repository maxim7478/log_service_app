import axios from 'axios'

const axiosInstance = (headerToken = false) => {
  const $axios = axios.create({
    baseURL: import.meta.env.VITE_BASE_URL,
  });
  return $axios;
};

export default axiosInstance;