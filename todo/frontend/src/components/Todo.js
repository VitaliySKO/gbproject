import React from "react"
import {Link} from "react-router-dom";


const TodoItem = ({todo}) =>{
    return(
        <tr>
            <td>{todo.id}</td>
            <td>{todo.name_todo}</td>
            <td>{todo.project}</td>
            <td>{todo.user}</td>
        </tr>
    )
}

const TodoList = ({todos}) =>{

    return(
        <table>
            <th>ID</th>
            <th>Name</th>
            <th>Project</th>
            <th>User</th>
            {todos.map((todo) => < TodoItem todo={todo} />)}
        </table>
    )
}

export default TodoList;