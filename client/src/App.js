import React, {useEffect} from 'react';
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import './App.css';
import Topheader from './Components/Topheader'
import Navigation from './Components/Navigation';
import Footer from './Components/Footer';
import HomePage from './Components/HomePage';
import UserProfile from './Components/UserProfile';
import BlogPost from './Components/BlogPost';
import CreateEditPost from './Components/CreateEditPost';
import Login from './Components/Login';
import Fashion from './Components/Fashion';
import Register from './Components/Register';

function App() {
    const [loggedInUser, setLoggedInUser] = React.useState(null);

    useEffect(() => {
        if (localStorage.getItem('token')) {
            if (localStorage.getItem('user')) {
                const user = JSON.parse(localStorage.getItem('user'));
                setLoggedInUser(user);
            }
        }
    }, []);

    return (
        <Router>
            <Topheader/>
            <Navigation loggedInUser={loggedInUser}/>
            <Routes>
                <Route path="/" element={<HomePage/>}/>
                <Route path="/user/:username" element={<UserProfile/>}/>
                <Route path="/post/:postId" element={<BlogPost/>}/>
                <Route path="/create" element={<CreateEditPost/>}/>
                <Route path="/edit/:postId" element={<CreateEditPost/>}/>
                <Route path="/login" element={<Login loggedInUser={loggedInUser} setLoggedInUser={setLoggedInUser}/>}/>
                <Route path="/fashion" element={<Fashion/>}/>
                <Route path="/register" element={<Register loggedInUser={loggedInUser} setLoggedInUser={setLoggedInUser}/>}/>
            </Routes>
            <Footer/>
        </Router>
    );
}

export default App;