import React, {useEffect, useState} from 'react';
import axios from '../utils/api';
import {useNavigate} from "react-router-dom";

const Login = ({ loggedInUser, setLoggedInUser }) => {
    const navigate = useNavigate();
    if (loggedInUser) {
        navigate('/');
    }

    const [errorMessage, setErrorMessage] = useState('');

    const [formData, setFormData] = useState({
        email: '',
        password: '',
    });

    const loginRequest = async ({email, password}) => {
        await axios.post('/users/login', {email, password})
            .then((response) => {
                console.log(response)
                if (response.status === 200) {
                    setLoggedInUser(response.data);
                    localStorage.setItem('token', response.data.access_token);
                    localStorage.setItem('user', JSON.stringify(response.data));
                }

                navigate('/');
            }).catch((error) => {
                // Handle error.
                console.log(error);

                if (error.response.status === 401 || error.response.status === 400) {
                    setErrorMessage(error.response.data.message);
                }
            });
    }

    const handleInputChange = (e) => {
        const {name, value} = e.target;
        setFormData({...formData, [name]: value});
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        const response = await loginRequest({
            email: formData.email,
            password: formData.password,
        });
    };

    return (
        <div className="container">
            <h1>Login</h1>
            <form onSubmit={handleSubmit}>
                <div className="mb-3">
                    <h3>{errorMessage}</h3>
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
                <button type="submit" onClick={handleSubmit} className="btn btn-primary">Login</button>
            </form>
        </div>
    );
};

export default Login;