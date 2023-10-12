import React, { useState } from 'react';
import { Navigate, useNavigate } from "react-router-dom";

import axios from "../utils/api";
const Register = () => {

  const navigate = useNavigate();

  const [registeredUser, setRegisteredUser] = useState({});
  const [errorMessage, setErrorMessage] = useState('');
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password: '',
    confirm_password: ''
  });

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };


  const loginRequest = async ({ email, username, password }) => {
    await axios.post('/users/register', { email, username, password })
        .then((response) => {
          // console.log(response)

          if (response.status === 201) {
            setRegisteredUser(response.data);
            localStorage.setItem('token', response.data.access_token);
            localStorage.setItem('user', JSON.stringify(response.data));

            navigate('/')
          }
        }).catch((error) => {
          // Handle error.
          console.log(error);
          if (error.response.status === 400) {
            setErrorMessage(error.response.data.message);
          }
        });
  }

  const handleSubmit = async (e) => {
    e.preventDefault();
    // Handle form submission for user registration
    // Implement your actual registration logic


    const response = await loginRequest({
      email: formData.email,
      username: formData.username,
      password: formData.password,
    });
  };

  return (
    <div className="container">
      <h1>Register</h1>
      <form onSubmit={handleSubmit}>
        <div className="mb-3">
          <h5>{errorMessage}</h5>
          <label htmlFor="username" className="form-label">Username</label>
          <input
            type="text"
            className="form-control"
            id="username"
            name="username"
            value={formData.username}
            onChange={handleInputChange}
          />
        </div>
        <div className="mb-3">
          <label htmlFor="email" className="form-label">Email</label>
          <input
            type="email"
            className="form-control"
            id="email"
            name="email"
            value={formData.email}
            onChange={handleInputChange}
          />
        </div>
        <div className="mb-3">
          <label htmlFor="password" className="form-label">Password</label>
          <input
            type="password"
            className="form-control"
            id="password"
            name="password"
            value={formData.password}
            onChange={handleInputChange}
          />
        </div>
        <div className="mb-3">
          <label htmlFor="confirmPassword" className="form-label">Confirm Password</label>
          <input
            type="password"
            className="form-control"
            id="confirm_password"
            name="confirm_password"
            value={formData.confirm_password}
            onChange={handleInputChange}
          />
        </div>
        <button type="submit" className="btn btn-primary">Register</button>
      </form>
    </div>
  );
};

export default Register;