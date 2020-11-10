<template>
  <Navbar></Navbar>
    <div class="container">
      <div class="todo-wrapper">
        <div class="todo-content">
          <div class="todo-content-title">
            <h2>Your todos</h2>
          </div>
          <TodosList></TodosList>
          <AddTodo></AddTodo>
        </div>
      </div>
    </div>
</template>


<script>
import Navbar from '../components/Navbar'
import AddTodo from '../components/AddTodo'
import TodosList from '../components/TodosList'
export default {
  name: 'Home',
  components: {
    Navbar,
    AddTodo,
    TodosList,
  },
};
</script>

<style lang="scss">
$base_font: sans-serif;

* { margin: 0; padding: 0 }

html, body {
  min-height: 100%;
  height: 100%;
}

body {
  background: #f5f5f5;
  font-family: $base_font;
  font-size: 14px;
}

.container {
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-flow: row wrap;
}

.todo-wrapper {
  background: #fff;
  border-radius: 6px;
  box-shadow: 0 0 40px rgba(0,0,0,.1);
  width: 300px;
}

.todo-content {
  .todo-content-title {
    padding: 20px;
    h2 {
      font-size: 1.7em;
      font-weight: normal;
      color: #4C4646;
    }
  }
}
</style>
