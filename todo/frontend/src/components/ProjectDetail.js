import React from "react"
import {Link, useParams} from "react-router-dom";


const ProjectItem = ({project, users}) =>{
    return(
        <tr>
            <td>{project.id}</td>
            <td>
                <Link to={`/projects/${project.id}`}>{project.name_project}</Link>
            </td>
            <td>{project.url_project}</td>
            <td>{project.users}</td>
            {/*<td>*/}
            {/*    {project.users.map((userID) =>{return users.find((user) => user.id == userID).username + ', '})}*/}
            {/*</td>*/}
        </tr>
    )
}



const ProjectDetailList = ({projects, users}) =>{

    let{id} = useParams();
    let filtered_items = projects.filter((project) => project.id == id)

    return(
        <table>
            <th>Name</th>
            <th>Url</th>
            <th>User ID</th>
            <th>User Name</th>
            {filtered_items.map((project) => < ProjectItem project={project} users={users}/>)}
        </table>
    )
}

export default ProjectDetailList;