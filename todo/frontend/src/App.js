import logo from './logo.svg';
import './App.css';
import React from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import {HashRouter, Route, Switch} from "react-router-dom";
import NaviBar from "./components/Menu";
import Footer from "./components/Footer";
import UserList from "./components/User";
import ProjectList from "./components/Project";
import NotFound404 from "./components/NotFound404";
import TodoList from "./components/Todo";
import ProjectDetailList from "./components/ProjectDetail";


class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'projects': [],
            'todos':[]
        }
    }
    componentDidMount(){
        axios.get('http://127.0.0.1:8000/api/users/').then(
            response =>{
                const users = response.data
                this.setState(
                    {
                        'users': users
                    }
                )
            }
        ).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/project/').then(
            response =>{
                const projects = response.data
                this.setState(
                    {
                        'projects': projects
                    }
                )
            }
        ).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/todo/').then(
            response =>{
                const todos = response.data
                this.setState(
                    {
                        'todos': todos
                    }
                )
            }
        ).catch(error => console.log(error))
    }
    render(){
        return (
            <div>
                <HashRouter>
                    <NaviBar/>
                    <Switch>
                        <Route exact path='/' component={() => <UserList users={this.state.users}/>} />
                        <Route exact path='/projects' component={() => <ProjectList projects={this.state.projects} />} />
                        <Route exact path='/todo' component={() => <TodoList todos={this.state.todos} />} />
                        <Route path='/projects/:id'>
                            <ProjectDetailList projects={this.state.projects} users={this.state.users}/>
                        </Route>

                        <Route component={NotFound404} />
                    </Switch>
                </HashRouter>
                {/*<Footer />*/}
            </div>
        );
    }
}

export default App;
