import logo from './logo.svg';
import './App.css';
import React from 'react';
import axios from 'axios';
import Cookies from "universal-cookie/lib";
import 'bootstrap/dist/css/bootstrap.min.css';
import {HashRouter, Link, Route, Switch} from "react-router-dom";
import NaviBar from "./components/Menu";
import Footer from "./components/Footer";
import UserList from "./components/User";
import ProjectList from "./components/Project";
import NotFound404 from "./components/NotFound404";
import TodoList from "./components/Todo";
import ProjectDetailList from "./components/ProjectDetail";
import LoginForm from "./components/LoginForm";
import {Button, Container, Nav, Navbar, NavLink} from "react-bootstrap";

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'projects': [],
            'todos': [],
            'token': '',
            'login': '',
        }
    }

    set_token(token){
        // console.log(token)
        const  cookies = new Cookies()
        cookies.set('token', token)
        this.setState({'token': token}, () => this.load_data())
    }

    is_auth(){
        return !!this.state.token
    }

    logout(){
        this.set_token('')
    }

    get_token_from_storage(){
        const  cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({'token': token}, () => this.load_data())
    }

    get_token(username, password){
        this.setState({'login': username})
        const  cookies = new Cookies()
        const data = {username:username, password:password}
        axios.post('http://127.0.0.1:8000/api-token-auth/', data).then(
            response =>{
                this.set_token(response.data['token'])
            }
        ).catch(error => alert("Неверный логин или пароль"))
    }

    load_data(){
        const headers = this.get_headers()
        axios.get('http://127.0.0.1:8000/api/users/', {headers}).then(
            response =>{
                const users = response.data
                this.setState(
                    {
                        'users': users
                    }
                )
            }
        ).catch(error => {
            console.log(error)
            this.setState({users:[], login: ''})
        })

        axios.get('http://127.0.0.1:8000/api/project/', {headers}).then(
            response =>{
                const projects = response.data
                this.setState(
                    {
                        'projects': projects
                    }
                )
            }
        ).catch(error => {
            console.log(error)
            this.setState({projects:[], login: ''})
        })

        axios.get('http://127.0.0.1:8000/api/todo/', {headers}).then(
            response =>{
                const todos = response.data
                this.setState(
                    {
                        'todos': todos
                    }
                )
            }
        ).catch(error => {
            console.log(error)
            this.setState({todos:[], login: ''})
        })
    }

    get_headers(){
        let headers = {
            'Content-Type': 'application/json'
        }
        if (this.is_auth()){
            headers['Authorization'] = 'Token ' + this.state.token
        }
        return headers
    }

    componentDidMount(){
        this.get_token_from_storage()
        // this.load_data()
    }
    render(){
        return (
            <div>
                <HashRouter>
                    {/*<NaviBar/>*/}
                    <Navbar collapseOnSelect expand="lg" bg="dark" variant="dark">
                        <Navbar.Brand>GB Project</Navbar.Brand>
                        <Navbar.Toggle aria-controls="respensive-navbar-nav"/>
                        <Navbar.Collapse id="respensive-navbar-nav">
                            <Nav className="mr-auto">
                                <Nav.Link href="#/">Users</Nav.Link>
                                <Nav.Link href="#projects">Projects</Nav.Link>
                                <Nav.Link href="#todo">Todo</Nav.Link>
                            </Nav>
                            <Nav>
                                {this.is_auth() ? <Button variant="primary" onClick={() => this.logout()}>Log Out</Button> :
                                    <Link to='/login'><Button variant="primary">Log In</Button></Link>}
                                <Navbar.Text>{this.state.login}</Navbar.Text>
                            </Nav>
                        </Navbar.Collapse>
                    </Navbar>
                    <Switch>
                        <Route exact path='/' component={() => <UserList users={this.state.users}/>} />
                        <Route exact path='/projects' component={() => <ProjectList projects={this.state.projects} />} />
                        <Route exact path='/todo' component={() => <TodoList todos={this.state.todos} />} />
                        <Route exact path='/login' component={() => <LoginForm get_token={(username, password) => this.get_token(username,password)}/>} />
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
