import streamlit as st
from modules import functions
st.title("ToDo App")
st.write("This app is to increase your productivity")

todos = functions.get_todos()

#st.session_state.todo = False
#st.write(st.session_state)

def add_todo():
    #st.write(st.session_state['todo'])
    #st.write(todo)
    new_todo = st.session_state.todo + "\n"
    #st.write(new_todo)
    todos.append(new_todo)
    #st.write(todos)
    functions.write_todos(todos)    

for index,todo in enumerate(todos):
    #st.experimental_rerun()
    st.checkbox(f"{index+1}.{todo}",on_change=None,key='todo_checkbox_' + str(index))
st.text_input("ToDo for the list", placeholder="Enter todo here...", label_visibility="hidden", key='todo', on_change=add_todo)    

    
def get_selected_todo_checkbox():
    for i in st.session_state.keys():
        if (i.startswith('todo_checkbox_') and st.session_state[i]):
            selected = i.replace('todo_checkbox_','')
            #st.text_input("todo") = selected
            selected = selected.strip('\n')
            #todo = st.text_input("ToDo to add to list",value=selected,placeholder="Enter todo here...",label_visibility="visible",key="edit-todo")    
            #st.write(selected)
            st.write(todos[int(selected)])
'''            
col1, col2, col3 = st.columns(3)
with col1:
    add = st.button("Add todo to list")
with col2:    
    edit = st.button("Edit a todo",on_click=get_selected_todo_checkbox())
    #st.experimental_rerun()
with col3:
    complete = st.button("Complete a todo item")
if add:
    #st.write(todo)
    new_todo = todo + "\n"
    st.write(new_todo)
    todos.append(new_todo)
    st.write(todos)
    functions.write_todos(todos)
'''