import { getAPI } from '../axios-api'

class TodoDataService {
  getAll(accessToken) {
    return getAPI.get("/todos/", { headers: {Authorization: `Bearer ${accessToken}`}});
  }

  get(uuid) {
    return getAPI.get(`/todo/${uuid}/`);
  }

  create(data, accessToken) {
    return getAPI.post("/todos/", data, { headers: {Authorization: `Bearer ${accessToken}`}});
  }

  update(uuid, data, accessToken) {
    return getAPI.put(`/todo/${uuid}/`, data, { headers: {Authorization: `Bearer ${accessToken}`}});
  }

  delete(uuid, accessToken) {
    return getAPI.delete(`/todo/${uuid}/`, { headers: {Authorization: `Bearer ${accessToken}`}});
  }

  deleteAll() {
    return getAPI.delete(`/todos/`);
  }
}

export default new TodoDataService();
