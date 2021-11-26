import React from "react";
import {Container, Nav, Navbar} from "react-bootstrap";


export default function NaviBar(){
    return (
    <>
        <Navbar collapseOnSelect expand="lg" bg="dark" variant="dark">
            <Navbar.Brand>GB Project</Navbar.Brand>
            <Navbar.Toggle aria-controls="respensive-navbar-nav"/>
            <Navbar.Collapse id="respensive-navbar-nav">
                <Nav className="mr-auto">
                    <Nav.Link>Home</Nav.Link>
                    <Nav.Link>Page1</Nav.Link>
                    <Nav.Link>Page2</Nav.Link>
                </Nav>
            </Navbar.Collapse>
        </Navbar>
    </>
    )
}