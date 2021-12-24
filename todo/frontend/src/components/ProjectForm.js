import React from "react";

class ProjectForm extends React.Component{
    constructor(props) {
        super(props);
        this.state = {
            name_project: '',
            url_project: '',
            users: [],
        }
    }

    handleChange(event){
        this.setState(
            {
                [event.target.name]: event.target.value
            }
        )
    }

    handleUserChange(event) {
        if (!event.target.selectedOptions) {
            this.setState({
                'users': []
            })
            return;
        }
        let users = []
        for(let i = 0; i<event.target.selectedOptions.length; i++){
            users.push(event.target.selectedOptions.item(i).value)
        }
        this.setState({
            'users': users
        })
    }


    handleSubmit(event){
        //console.log(this.state.name_project + ' ' + this.state.users)
        this.props.createProject(this.state.name_project, this.state.url_project, this.state.users)
        event.preventDefault()
    }

    render() {
        return(
            <form onSubmit={(event) => this.handleSubmit(event)}>
                <div className="form-group">
                    <label htmlFor="name_project">name project</label>
                    <input type="text" className="form" name="name_project" value={this.state.name_project}
                           onChange={(event) => this.handleChange(event)}/>
                </div>
                <div className="form-group">
                    <label htmlFor="url_project">url project</label>
                    <input type="text" className="form" name="url_project" value={this.state.url_project}
                           onChange={(event) => this.handleChange(event)}/>
                </div>
                <div className="form-group">
                    <label htmlFor="users">users</label>
                    <select className="form" name="users" multiple onChange={(event) => this.handleUserChange(event)}>
                    {this.props.users.map((item) => <option value={item.id}>{item.username}</option>)}
                    </select>
                </div>
                <input type="submit" value="Save"/>
            </form>
        );
    }
}

export default ProjectForm;