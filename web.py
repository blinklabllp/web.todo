import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo_local = st.session_state["new_todo"] + "\n"
    todos.append(todo_local)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""


st.title("My ToDo App")
st.header("This is my ToDo App")
st.write("This app is to increase your productivity.")

# Load all the todos
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="New ToDo", placeholder="Add new todo...", on_change=add_todo,
              key='new_todo', label_visibility='hidden')
