import React from "react";
import {Button, Container, Nav, Navbar, NavLink} from "react-bootstrap";
import {Link} from "react-router-dom";


export default function NaviBar(){
    return (
        <>
        <Navbar collapseOnSelect expand="lg" bg="dark" variant="dark">
            <Navbar.Brand>GB Project</Navbar.Brand>
            <Navbar.Toggle aria-controls="respensive-navbar-nav"/>
            <Navbar.Collapse id="respensive-navbar-nav">
                <Nav className="mr-auto">
                    <Nav.Link href="#/">Users</Nav.Link>
                    <Nav.Link href="#projects">Projects</Nav.Link>
                    <Nav.Link href="#todo">Todo</Nav.Link>
                </Nav>
                {/*<Nav>{this.is_auth() ? <Button variant="primary" onClick={() => this.logout()}>Log Out</Button> :*/}
                {/*    <Link to='/login'><Button variant="primary">Log In</Button></Link>}*/}
                {/*</Nav>*/}
        </Navbar.Collapse>
        </Navbar>
</>
)
}