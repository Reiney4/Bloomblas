import React from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css';

const Navigation = ({ loggedInUser }) => {
  return (
    <nav className="navbar navbar-expand-lg bg-body-tertiary" style={{ backgroundColor: '#ffffff', color: 'black' }}>
      <div className="container">
        <Link className="navbar-brand" to="/">
          <img
            src="data:image/png;base64,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"
            alt="Logo"
            width="50"
            height="50"
            className="d-inline-block align-top mr-2"
          />
         
        </Link>
        <div className="navbar-collapse">
          <ul className="navbar-nav">
            <li className="nav-item">
              <Link className="nav-link" to="/">
                Home
              </Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/create">
                Create Post
              </Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/fashion">
                Fashion
              </Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/">
                Lifestyle
              </Link>
            </li>
          </ul>
        </div>

        { loggedInUser ? (
            <h5>{loggedInUser.user_email}</h5>
        ) : (
            <div className="ml-auto">
              <ul className="navbar-nav">
                <li className="nav-item">
                  <Link id="Login" className="btn btn-primary" to="/login">
                    Login
                  </Link>
                </li>
                <li className="nav-item">
                  <Link id="Login" className="btn btn-primary" to="/register">
                    Register
                  </Link>
                </li>
              </ul>
            </div>
        ) }
      </div>
    </nav>
  );
};

export default Navigation;