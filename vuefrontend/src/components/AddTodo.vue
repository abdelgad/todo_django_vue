<template>
  <div class="submit-form">
    <form v-on:submit.prevent="saveTodo">
        <div class="input-field">
          <input class="value-input" type="text" name="value" v-model="todo.value" placeholder="Enter new task">
        </div>
      <div class="action">
        <button class="addTodoBtn" type="submit">Add</button>
      </div>
    </form>
  </div>
</template>

<script>
import TodoDataService from "../services/TodoDataService"

export default {
  name: "AddTodo",
  data() {
    return {
      todo: {
        value: ""
        //add some other attributes
      },
    }
  },
  methods: {
    saveTodo() {
      var data = {
        value: this.todo.value,
      };

      TodoDataService.create(data, this.$store.state.accessToken)
        .then(response => {
          this.$store.state.todoslist.push(response.data)
          this.todo.value = '';
          console.log(response.data);
        })
        .catch(e => {
          console.log(e);
        });
    },
  }
};
</script>

<style lang="scss">
.submit-form
{
  border-top: 1px solid #f1f1f1;
  padding: 15px 20px;
  position: relative;
}

.value-input
{
  border:none;
  width: 100%;
  min-width: 100%;
  margin: 0 0 10px;
  padding: 0;
  line-height: 2em;
}

.addTodoBtn{
  display:inline-block;
  padding:0.35em 1.2em;
  border:0.1em solid #f1f1f1;
  margin:0 0.3em 0.3em 0;
  border-radius:0.20em;
  box-sizing: border-box;
  font-weight:300;
  color:#000000;
  text-align:center;
  transition: all 0.2s;
}
</style>
