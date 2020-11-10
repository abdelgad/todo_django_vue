import axios from 'axios'

const getAPI = axios.create({
  baseURL: 'http://127.0.0.1:8000/api',
  headers: {
    "Content-Type": "application/json"
  },
  timeout: 1000,
})

export { getAPI }
