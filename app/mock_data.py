from faker import Faker
from typing import List, Dict
import random

fake = Faker()

# Generate mock users


def generate_users(count: int = 10) -> List[Dict]:
    users = []
    for i in range(1, count + 1):
        users.append({
            "id": i,
            "name": fake.name(),
            "username": fake.user_name(),
            "email": fake.email(),
            "address": {
                "street": fake.street_address(),
                "suite": fake.building_number(),
                "city": fake.city(),
                "zipcode": fake.zipcode(),
                "geo": {
                    "lat": fake.latitude(),
                    "lng": fake.longitude()
                }
            },
            "phone": fake.phone_number(),
            "website": fake.url(),
            "company": {
                "name": fake.company(),
                "catchPhrase": fake.catch_phrase(),
                "bs": fake.bs()
            }
        })
    return users

# Generate mock posts


def generate_posts(users: List[Dict], count_per_user: int = 3) -> List[Dict]:
    posts = []
    post_id = 1
    for user in users:
        for _ in range(count_per_user):
            posts.append({
                "id": post_id,
                "userId": user["id"],
                "title": fake.sentence(nb_words=6),
                "body": fake.paragraph(nb_sentences=3)
            })
            post_id += 1
    return posts

# Generate mock comments


def generate_comments(posts: List[Dict], count_per_post: int = 2) -> List[Dict]:
    comments = []
    comment_id = 1
    for post in posts:
        for _ in range(count_per_post):
            comments.append({
                "id": comment_id,
                "postId": post["id"],
                "name": fake.name(),
                "email": fake.email(),
                "body": fake.paragraph(nb_sentences=2)
            })
            comment_id += 1
    return comments

# Generate mock albums


def generate_albums(users: List[Dict], count_per_user: int = 2) -> List[Dict]:
    albums = []
    album_id = 1
    for user in users:
        for _ in range(count_per_user):
            albums.append({
                "id": album_id,
                "userId": user["id"],
                "title": fake.sentence(nb_words=4)
            })
            album_id += 1
    return albums

# Generate mock photos


def generate_photos(albums: List[Dict], count_per_album: int = 5) -> List[Dict]:
    photos = []
    photo_id = 1
    for album in albums:
        for _ in range(count_per_album):
            photos.append({
                "id": photo_id,
                "albumId": album["id"],
                "title": fake.sentence(nb_words=3),
                "url": fake.image_url(),
                "thumbnailUrl": fake.image_url()
            })
            photo_id += 1
    return photos

# Generate all mock data


def generate_all_mock_data():
    users = generate_users(10)
    posts = generate_posts(users)
    comments = generate_comments(posts)
    albums = generate_albums(users)
    photos = generate_photos(albums)

    return {
        "users": users,
        "posts": posts,
        "comments": comments,
        "albums": albums,
        "photos": photos
    }


mock_data = generate_all_mock_data()
