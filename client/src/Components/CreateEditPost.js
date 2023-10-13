import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';

const CreateEditPost = () => {
  const { postId } = useParams();
  const isEditing = !!postId;
  const [post, setPost] = useState({
    title: '',
    content: '',
  });

  useEffect(() => {
    // Fetch the post details if in edit mode
    if (isEditing) {
      // Replace this with your actual data fetching logic
    }
  }, [postId, isEditing]);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setPost({ ...post, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Handle form submission for creating/editing a post
    // Implement your actual data posting/updating logic
  };

  return (
    <div className="container">
      <h1>{isEditing ? 'Edit Post' : 'Create Post'}</h1>
      <form onSubmit={handleSubmit}>
        <div className="mb-3">
          <label htmlFor="title" className="form-label">Title</label>
          <input
            type="text"
            className="form-control"
            id="title"
            name="title"
            value={post.title}
            onChange={handleInputChange}
          />
        </div>
        <div className="mb-3">
          <label htmlFor="content" className="form-label">Content</label>
          <textarea
            className="form-control"
            id="content"
            name="content"
            value={post.content}
            onChange={handleInputChange}
          ></textarea>
        </div>
        <button type="submit" className="btn btn-primary">
          {isEditing ? 'Save Changes' : 'Create Post'}
        </button>
      </form>
    </div>
  );
};

export default CreateEditPost;
