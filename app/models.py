from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    username: str
    email: str
    address: dict
    phone: str
    website: str
    company: dict


class Post(BaseModel):
    id: int
    userId: int
    title: str
    body: str


class Comment(BaseModel):
    id: int
    postId: int
    name: str
    email: str
    body: str


class Album(BaseModel):
    id: int
    userId: int
    title: str


class Photo(BaseModel):
    id: int
    albumId: int
    title: str
    url: str
    thumbnailUrl: str
