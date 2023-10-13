import React, { useEffect, useState } from 'react';
import './Homepage.css';

const HomePage = () => {
  const [posts, setPosts] = useState([]);
  const [email, setEmail] = useState('');

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(
          'https://api.npoint.io/e6bfa83e4e0c07b6877f/blog_posts'
        );
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }

        const data = await response.json();
        setPosts(data || []);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData()
  }, []);

  console.log(posts);

  const handleEmailChange = (e) => {
    setEmail(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Add your subscription logic here
    console.log(`Subscribed with email: ${email}`);
    setEmail(''); // Clear the email input after submission
  };

  return (
    <div>
      <div id="landing" className="card text-bg-dark">
        <img
          id="landing_img"
          src="https://media.istockphoto.com/id/1129342275/photo/enjoying-his-favorite-music.jpg?b=1&s=612x612&w=0&k=20&c=QUcz3d1U-v1odGWHSCN_junv7Rrr-jJmYY7blz_pNYY="
          className="card-img"
          alt="Fashion and Lifestyle"
        />
        <div className="card-img-overlay">
          <h5 id="text-title" className="card-title">
            Blog for Fashion &amp;<br /> Lifestyle Lovers
          </h5>
          <p className="card-text">
            Step into the stylish world of fashion and lifestyle aficionados!{' '}
            <br />
            Explore the art of self-expression, trendsetting, and the joy of
            living life to the fullest. <br />
            Join us in celebrating those who turn every day into a statement
            and every outfit into a canvas.<br />
            Welcome to the world of fashion and lifestyle lovers!
          </p>
        </div>
      </div>

      <div>
        <h1 id="topics">Latest Topics</h1>
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
                        alt={post.title}
                      />
                    </div>
                    <div className="col-md-8">
                      <div className="card-body">
                        <h5 className="card-title">{post.title}</h5>
                        <p className="card-text">{post.content_description}</p>
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

      <div>
        <h2 id="subscribe-title">Subscribe to Our Newsletter</h2>
        <p id="subscribe-description">
          Stay up-to-date with the latest fashion and lifestyle trends.
        </p>
        <form onSubmit={handleSubmit} id="subscribe-form">
          <div className="input-group mb-3">
            <input
              type="email"
              className="form-control"
              placeholder="Your Email Address"
              aria-label="Your Email Address"
              aria-describedby="subscribe-button"
              value={email}
              onChange={handleEmailChange}
            />
            <button
              className="btn btn-primary"
              type="submit"
              id="subscribe-button"
            >
              Subscribe
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default HomePage;