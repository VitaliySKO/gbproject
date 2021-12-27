import React from "react"
import {Link} from "react-router-dom";


const TodoItem = ({todo, deleteTodo}) =>{
    return(
        <tr>
            <td>{todo.id}</td>
            <td>{todo.name_todo}</td>
            <td>{String(todo.status_todo)}</td>
            <td>{todo.project}</td>
            <td>{todo.user}</td>
            <td>
                <button onClick={() => deleteTodo(todo.id)} type='button'>
                    Delete
                </button>
            </td>
        </tr>
    )
}

const TodoList = ({todos, deleteTodo}) =>{

    return(
        <div>
        <table>
            <th>ID</th>
            <th>Name</th>
            <th>Status todo</th>
            <th>Project</th>
            <th>User</th>
            <th></th>
            {todos.map((todo) => < TodoItem todo={todo} deleteTodo={deleteTodo}/>)}
        </table>
        <Link to='/todo/create'>Create</Link>
        </div>
    )
}

export default TodoList;