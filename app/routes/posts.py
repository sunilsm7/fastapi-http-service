from fastapi import APIRouter, Request, Query, Body
from fastapi import HTTPException, Depends, status
from mock_data import mock_posts, mock_comments, mock_albums, mock_photos
from typing import List, Optional
from models import Post, Comment, Album, Photo

router = APIRouter()

# posts

@router.get("/posts", response_model=List[Post])
def get_posts(
        page: int = Query(1, ge=1),
        limit: int = Query(10, ge=1, le=100)
):
    start = (page - 1) * limit
    end = start + limit
    return mock_posts[start:end]


@router.get("/posts/{post_id}", response_model=Post)
def get_post(post_id: int):
    post = next((p for p in mock_posts if p["id"] == post_id), None)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@router.post("/posts", response_model=Post)
def create_post(post: Post):
    new_id = max(p["id"] for p in mock_posts) + 1
    new_post = {**post.dict(), "id": new_id}
    mock_posts.append(new_post)
    return new_post


@router.put("/posts/{post_id}", response_model=Post)
def update_post(post_id: int, post: Post):
    index = next((i for i, p in enumerate(mock_posts) if p["id"] == post_id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="Post not found")
    mock_posts[index] = {**post.dict(), "id": post_id}
    return mock_posts[index]


@router.delete("/posts/{post_id}")
def delete_post(post_id: int):
    global mock_posts
    mock_posts = [p for p in mock_posts if p["id"] != post_id]
    return {"message": "Post deleted"}


# comments
@router.get("/comments", response_model=List[Comment])
def get_comments(postId: Optional[int] = Query(None)):
    if postId:
        return [c for c in mock_comments if c["postId"] == postId]
    return mock_comments


@router.post("/comments", response_model=Comment)
def create_comment(comment: Comment):
    new_id = max(p["id"] for p in mock_comments) + 1
    new_comment = {**comment.dict(), "id": new_id}
    mock_comments.append(new_comment)
    return new_comment


@router.put("/comments/{comment_id}", response_model=Comment)
def update_comment(comment_id: int, comment: Comment):
    index = next((i for i, p in enumerate(mock_comments) if p["id"] == comment_id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    mock_comments[index] = {**comment.dict(), "id": comment_id}
    return mock_comments[index]


@router.delete("/comments/{comment_id}")
def delete_comment(comment_id: int):
    global mock_comments
    mock_comments = [p for p in mock_comments if p["id"] != comment_id]
    return {"message": "Comment deleted"}

# albums

@router.get("/albums", response_model=List[Album])
def get_albums():
    return mock_albums


@router.get("/albums/{album_id}", response_model=Album)
def get_album(album_id: int):
    album = next((p for p in mock_albums if p["id"] == album_id), None)
    if not album:
        raise HTTPException(status_code=404, detail="Album not found")
    return album


@router.post("/albums", response_model=Album)
def create_album(album: Album):
    new_id = max(p["id"] for p in mock_albums) + 1
    new_album = {**album.dict(), "id": new_id}
    mock_albums.append(new_album)
    return new_album


@router.put("/albums/{album_id}", response_model=Album)
def update_album(album_id: int, post: Album):
    index = next((i for i, p in enumerate(mock_albums) if p["id"] == album_id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="Album not found")
    mock_albums[index] = {**post.dict(), "id": album_id}
    return mock_albums[index]


@router.delete("/albums/{album_id}")
def delete_album(album_id: int):
    global mock_albums
    mock_albums = [p for p in mock_albums if p["id"] != album_id]
    return {"message": "Album deleted"}


# photos


@router.get("/photos", response_model=List[Photo])
def get_photos():
    return mock_photos


@router.get("/photos/{photo_id}", response_model=Photo)
def get_photo(photo_id: int):
    photo = next((p for p in mock_photos if p["id"] == photo_id), None)
    if not photo:
        raise HTTPException(status_code=404, detail="Photo not found")
    return photo


@router.post("/photos", response_model=Photo)
def create_photo(photo: Photo):
    new_id = max(p["id"] for p in mock_photos) + 1
    new_photo = {**photo.dict(), "id": new_id}
    mock_photos.append(new_photo)
    return new_photo


@router.put("/photos/{photo_id}", response_model=Photo)
def update_aphoto(photo_id: int, photo: Photo):
    index = next((i for i, p in enumerate(mock_photos) if p["id"] == photo_id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="Photo not found")
    mock_photos[index] = {**photo.dict(), "id": photo_id}
    return mock_photos[index]


@router.delete("/photos/{photo_id}")
def delete_aphoto(photo_id: int):
    global mock_photos
    mock_photos = [p for p in mock_photos if p["id"] != photo_id]
    return {"message": "Photo deleted"}
