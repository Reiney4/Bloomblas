import React, { useEffect, useState } from 'react';
import './Homepage.css';

const Fashion = () => {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(
          'http://127.0.0.1:5555/blogposts'
        );
        console.log(response)
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }

        const data = await response.json();
        setPosts(data || []);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  console.log(posts);

  return (
    <div>

      <div>
        <h1 id="topics">Trending In Fashion</h1>
        <div className="row row-cols-1 row-cols-md-2 g-4">
          {posts.length > 0 ? (
            posts.map((post, index) => (
              <div className="col" key={index}>
                <div className="card" style={{ maxWidth: '540px' }}>
                  <div className="row g-0">
                    <div className="col-md-4">
                      <img
                        src={post.image_link}
                        className="img-fluid rounded-start"
                        alt={post.name}
                      />
                    </div>
                    <div className="col-md-8">
                      <div className="card-body">
                        <h5 className="card-title">{post.title}</h5>
                        <p className="card-text">{post.description}</p>
                        <p className="card-text">
                          <small className="text-body-secondary">
                            Author: {post.author}
                          </small>
                        </p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            ))
          ) : (
            <p>No posts available.</p>
          )}
        </div>
      </div>
    </div>
  );
};

export default Fashion;