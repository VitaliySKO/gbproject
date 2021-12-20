import React from "react"
import {Link} from "react-router-dom";


const ProjectItem = ({project}) =>{
    return(
        <tr>
            <td>{project.id}</td>
            <td>
                <Link to={`/projects/${project.id}`}>{project.name_project}</Link>
            </td>
            <td>{project.url_project}</td>
            <td>{project.users}</td>
        </tr>
    )
}

const ProjectList = ({projects}) =>{

    return(
        <table>
            <th>ID</th>
            <th>Name</th>
            <th>Url</th>
            <th>User ID</th>
            {projects.map((project) => < ProjectItem project={project} />)}
        </table>
    )
}

export default ProjectList;