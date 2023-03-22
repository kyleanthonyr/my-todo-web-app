import streamlit as st

import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("Increase your productivity.")
st.text_input(label="Enter a todo: ",
              placeholder="Take over the world..",
              on_change=add_todo,
              key="new_todo")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]  # removes to-do from sessionstate dict
        st.experimental_rerun()  # refreshes the page

