from app import app
from models import Blogpost, User, User_blogposts, db
from faker import Faker
import random
from datetime import datetime  # Import datetime for timestamp

# Create a Faker instance
fake = Faker()

with app.app_context():
    # Clear existing data
    User_blogposts.query.delete()
    User.query.delete()
    Blogpost.query.delete()

    print("🦸‍♀️ Seeding blogposts...")

    blogposts_data = [
        {"name": "la fashion", "description": "gives French vibes"},
        {"name": "Bleeding ink", "description": "bringing your stories to life"},
        {"name": "The Blog Business", "description": "keeping you updated on the business world"},
        {"name": "Glam up", "description": "here to assert drip is for life"},
        {"name": "NatureScribblings", "description": "Nature is beautiful"},
        {"name": "Sage's corner", "description": "a look into Sage's fabulous lifestyle"},
        {"name": "Beauty secrets", "description": "Open a door to vast knowledge in skincare"},
        {"name": "Hiking Diary", "description": "Discover the world's best hiking grounds"},
        {"name": "Analog blog", "description": "Travel back to reminisce ancient cultures"},
        {"name": "Chocolate Fanatic", "description": "chocolate discovery "},
        {"name": "Seaman tales", "description": "underwater chronicles"},
        {"name": "City food", "description": "a plug to your go-to food places"},
        {"name": "Basqueparfum", "description": "let your scent tell your story"},
    ]

    new_blogposts = [
        {
            "title": "Healthy Eating Habits",
            "author": "Sophia Miller",
            "image_link": "https://media.istockphoto.com/id/1325578537/photo/happy-indian-mother-having-fun-with-her-daughter-outdoor-family-and-love-concept-focus-on-mum.jpg?b=1&s=612x612&w=0&k=20&c=SJ9XOGSV7al3uhCzrGZx6AiEdxk5AF_MO9o0h_ifyCg=",
            "content_description": "Tips and tricks for maintaining a balanced and healthy diet."
        },
        {
            "title": "Traveling on a Budget",
            "author": "Michael Brown",
            "image_link": "https://media.istockphoto.com/id/1358737791/photo/affectionate-mother-touching-noses-with-her-young-son.jpg?b=1&s=612x612&w=0&k=20&c=11IoXtZYAFJ4yj-2gsa8NRlgqBg4TxWlBdCCb7cuv6o=",
            "content_description": "Explore budget-friendly travel options without compromising on experiences."
        },
        {
            "title": "Mindful Living: Finding Inner Peace",
            "author": "Ava Wilson",
            "image_link": "https://example.com/mindfulness2.jpg",
            "content_description": "Practices and strategies for achieving mindfulness and inner peace in a fast-paced world."
        },
        {
            "title": "Fitness for a Better Life",
            "author": "Ethan Clark",
            "image_link": "https://media.istockphoto.com/id/1266364224/photo/father-helps-young-daughter-ride-skateboard.jpg?b=1&s=612x612&w=0&k=20&c=8qcErts6ZQ7NRujJaQ8XDSzuhBN3iUtHhHRKrZwADGc=",
            "content_description": "The importance of physical fitness and its positive impact on your overall well-being."
        },
        {
            "title": "DIY Home Decor Ideas",
            "author": "Olivia Turner",
            "image_link": "https://media.istockphoto.com/id/1324381802/photo/on-a-road-trip-with-our-dog.jpg?b=1&s=612x612&w=0&k=20&c=adZMYLDT8aEBwHhFiZoBiTjdUpTUdvS8hb07DOVcUo4=",
            "content_description": "Creative DIY projects to decorate your home on a budget."
        },
        {
            "title": "Gardening Tips for Urban Dwellers",
            "author": "Daniel Moore",
            "image_link": "https://media.istockphoto.com/id/1319763314/photo/mature-multiethnic-couple-laughing-and-embracing-at-home.jpg?b=1&s=612x612&w=0&k=20&c=xvVGN-GhUFmJl2MK5e9snC-kyY3GVJWDSMwc2P9kWLQ=",
            "content_description": "How to cultivate a green oasis in your city apartment."
        },
        {
            "title": "Healthy Relationships: Building Strong Connections",
            "author": "Mia Davis",
            "image_link": "https://media.istockphoto.com/id/1159094800/photo/mother-father-children-son-and-daughter-on-sunset.jpg?b=1&s=612x612&w=0&k=20&c=9jmKRfE4SNjKCLTYimpDFMI8NhHgNS73Bozbhrdc_T4=",
            "content_description": "Tips on nurturing and maintaining healthy relationships with loved ones."
        },
        {
            "title": "The Art of Time Management",
            "author": "Liam Smith",
            "image_link": "https://media.istockphoto.com/id/1308292203/photo/multiracial-women-doing-yoga-exercise-with-social-distance-for-coronavirus-outbreak-at-park.jpg?b=1&s=612x612&w=0&k=20&c=KQl4ANlBQFcFbaSTeuJ6mgql4-wIwPtzEBZ3BHdU8a8=",
            "content_description": "Effective time management techniques for improved productivity and work-life balance."
        },
        {
            "title": "Exploring Hobbies: Unleash Your Creativity",
            "author": "Nora Johnson",
            "image_link": "https://media.istockphoto.com/id/1300273437/photo/and-then-you-came-along-and-turned-my-life-around.jpg?b=1&s=612x612&w=0&k=20&c=_sTn5Q80pP0tTeWxj7YaFYcPYsovnXl8Ai0FIpvV0uQ=",
            "content_description": "Discover the benefits of pursuing hobbies and exploring your creative side."
        },
        {
            "title": "Sustainable Living: Eco-Friendly Choices",
            "author": "Henry White",
            "image_link": "https://media.istockphoto.com/id/1285301614/photo/young-man-arms-outstretched-by-the-sea-at-sunrise-enjoying-freedom-and-life-people-travel.jpg?b=1&s=612x612&w=0&k=20&c=LIHDLfQsTnhmdQXAXjwo-NN3DW2RaXHaRSCTvjtNDSY=",
            "content_description": "How to adopt a more sustainable and eco-friendly lifestyle in everyday practices."
        }
    ]

    for data in new_blogposts:
        # Provide valid values for 'ratings' and 'updated_at' when inserting a blog post
        blogpost_data = {
            "title": data["title"],
            "description": data["content_description"],
            "author": data["author"],
            "image_link": data["image_link"],
            "ratings": "Good",  # Provide a valid rating value
            "updated_at": datetime.utcnow(),  # Provide the current timestamp
        }
        blogpost = Blogpost(**blogpost_data)
        db.session.add(blogpost)

    db.session.commit()

    print("🦸‍♀️ Adding users...")

    # Generate and add fake users
    for _ in range(12):
        username = fake.user_name()
        email = fake.email()
        user = User(username=username, email=email)
        db.session.add(user)

    db.session.commit()

    print("🦸‍♀️ Adding blogposts to users...")

    ratings = ["Good", "Awesome", "Fantastic"]

    users = User.query.all()
    blogposts = Blogpost.query.all()

    for user in users:
        for _ in range(random.randint(1, 3)):
            blogpost = random.choice(blogposts)
            rating = random.choice(ratings)

            user_blogpost = User_blogposts(user_id=user.id, blogpost_id=blogpost.id, rating=rating)
            db.session.add(user_blogpost)

    db.session.commit()

    print("🦸‍♀️ Done seeding!")