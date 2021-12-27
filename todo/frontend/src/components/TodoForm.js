import React from "react";


class TodoForm extends React.Component{
    constructor(props) {
        super(props);
        this.state = {
            name_todo: '',
            text_todo: '',
            status_todo: false,
            project: props.projects[0].id,
            user: props.users[0].id,
        }
    }

    handleChange(event){
        this.setState(
            {
                [event.target.name]: event.target.value
            }
        )
    }

    handleSubmit(event){
        console.log(this.state.name_todo + ' ' + this.state.project + ' ' + this.state.status_todo)
        this.props.createTodo(this.state.name_todo, this.state.text_todo, this.state.status_todo, this.state.project, this.state.user)
        event.preventDefault()
    }

    render() {
        return(
            <form onSubmit={(event) => this.handleSubmit(event)}>
                <div className="form-group">
                    <label htmlFor="name_todo">name todo</label>
                    <input type="text" className="form" name="name_todo" value={this.state.name_todo}
                           onChange={(event) => this.handleChange(event)}/>
                </div>
                <div className="form-group">
                    <label htmlFor="text_todo">text todo</label>
                    <input type="text" className="form" name="text_todo" value={this.state.text_todo}
                           onChange={(event) => this.handleChange(event)}/>
                </div>
                <div className="form-group">
                    <label htmlFor="project">project</label>
                    <select className="form" name="project" onChange={(event) => this.handleChange(event)}>
                    {this.props.projects.map((item) => <option value={item.id}>{item.name_project}</option>)}
                    </select>
                </div>

                <div className="form-group">
                    <label htmlFor="user">user</label>
                    <select className="form" name="user" onChange={(event) => this.handleChange(event)}>
                    {this.props.users.map((item) => <option value={item.id}>{item.username}</option>)}
                    </select>
                </div>
                <input type="submit" value="Save"/>
            </form>
        );
    }
}

export default TodoForm;