<template>
  <ul class="todo-list">
    <li
    class="todo-item"
    :class="[{ active: index == currentIndex }, {checkedTodo: todo.checked == true}]"
    v-for="(todo, index) in todoslist"
    :key="index"
    @click="setActiveTodo(todo, index)"
    >
      <p class="text">{{ todo.value }}</p>
      <button class="btn" v-if="currentTodo !== null && currentTodo.checked && index == currentIndex" @click="updateChecked(false)">
        Uncheck
      </button>

      <button class="btn" v-if="currentTodo !== null && !currentTodo.checked && index == currentIndex" @click="updateChecked(true)">
        Check
      </button>

      <button class="btn" v-if="currentTodo !== null && index == currentIndex" @click="deleteTodo()">
        Delete
      </button>
    </li>
  </ul>
</template>

<script>
import TodoDataService from "../services/TodoDataService";
import { mapState } from 'vuex'

export default {
  name: "TodosList",
  data() {
    return {
      currentTodo: null,
      currentIndex: -1,
      // title: ""
    };
  },
  computed: mapState(['todoslist']),
  methods: {
    retrieveTodos() {
      TodoDataService.getAll(this.$store.state.accessToken)
        .then(response => {
         this.$store.state.todoslist = response.data;
          console.log(response.data);
        })
        .catch(e => {
          console.log(e);
        });
    },

    resetActiveTodo() {
      this.currentTodo = null;
      this.currentIndex = -1;
    },

    setActiveTodo(todo, index) {
      this.currentTodo = todo;
      this.currentIndex = index;
      // console.log(this.currentTodo);
    },

    updateChecked(status) {
      var data = {
        uuid: this.currentTodo.uuid,
        value: this.currentTodo.value,
        checked: status,
        owner: this.currentTodo.owner,
      };

      TodoDataService.update(this.currentTodo.uuid, data, this.$store.state.accessToken)
        .then(response => {
          this.currentTodo.checked = status;
          console.log(response.data);
        })
        .catch(e => {
          console.log(e);
        });
    },

    deleteTodo() {
      TodoDataService.delete(this.currentTodo.uuid, this.$store.state.accessToken)
        .then(response => {
          this.$store.state.todoslist.pop(response.data);
          this.resetActiveTodo();
          console.log(response.data);
        })
        .catch(e => {
          console.log(e);
        });
    },
  },
  created() {
    this.retrieveTodos();
  }
};
</script>

<style lang="scss">
.active
{
  background-color: #008B8B;
}

.todo-list {
  list-style: none;
  .todo-item {
    padding: 15px 20px;
    border-top: 1px solid #f1f1f1;
    position: relative;
    .text {
      position: relative;
      top: -2px;
    }
    &.checkedTodo
    {
      .text {
        color: #ccc;
        text-decoration: line-through;
      }
    }
  }
}

.btn{
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
  margin-top: 5px;
}
</style>
