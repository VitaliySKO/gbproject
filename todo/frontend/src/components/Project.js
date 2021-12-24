import React from "react"
import {Link} from "react-router-dom";


const ProjectItem = ({project, deleteProject}) =>{
    return(
        <tr>
            <td>{project.id}</td>
            <td>
                <Link to={`/projects/${project.id}`}>{project.name_project}</Link>
            </td>
            <td>{project.url_project}</td>
            <td>{project.users}</td>
            <td>
                <button onClick={() => deleteProject(project.id)} type='button'>
                    Delete
                </button>
            </td>
        </tr>
    )
}

const ProjectList = ({projects, deleteProject}) =>{

    return(
        <div>
        <table>
            <th>ID</th>
            <th>Name</th>
            <th>Url</th>
            <th>User ID</th>
            {projects.map((project) => < ProjectItem project={project} deleteProject={deleteProject}/>)}
        </table>
        <Link to='/projects/create'>Create</Link>
        </div>
    )
}

export default ProjectList;