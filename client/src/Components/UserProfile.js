import React from 'react';
import { useParams } from 'react-router-dom';

const UserProfile = () => {
  const { username } = useParams();

  // Fetch user details and their posts
  // Replace this with your actual data fetching logic

  return (
    <div className="container">
      <h1>User Profile: {username}</h1>
      {/* Display user information and their posts */}
    </div>
  );
};

export default UserProfile;
