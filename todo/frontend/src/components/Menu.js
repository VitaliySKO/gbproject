import React from "react";
import {Container, Nav, Navbar, NavLink} from "react-bootstrap";
import {Link} from "react-router-dom";


export default function NaviBar(){
    return (
    <>
        <Navbar collapseOnSelect expand="lg" bg="dark" variant="dark">
            <Navbar.Brand>GB Project</Navbar.Brand>
            <Navbar.Toggle aria-controls="respensive-navbar-nav"/>
            <Navbar.Collapse id="respensive-navbar-nav">
                <Nav className="mr-auto">
                    {/*<Nav.Link href='/'>Users</Nav.Link>*/}
                    {/*<Nav.Link href='/projects'>Projects</Nav.Link>*/}
                    {/*<Nav.Link href='/todo'>Todo</Nav.Link>*/}
                    <Nav.Link><Link to='/'>Users</Link></Nav.Link>
                    <Nav.Link><Link to='/projects'>Projects</Link></Nav.Link>
                    <Nav.Link><Link to='/todo'>Todo</Link></Nav.Link>
                </Nav>
            </Navbar.Collapse>
        </Navbar>
    </>
    )
}