import axiosInstance from '@/services/axiosInstance'
const $axios = axiosInstance();

export default {
  getLogData: async (params: any) => {
    try {
      const { data } = await $axios.get('/logs/pool', {
        params
      });
      return data;
    } catch (err) {
      console.log(err)
    }
  },
}