from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import (
    request_inspect, status_codes, auth_routes,
    response_format, dynamic_data, redirect, anything,
    users, posts
)

from mock_data import generate_all_mock_data


def create_app():
    app = FastAPI(
        title="FastAPI HTTP Test Service",
        description="API for interacting with HTTP requests",
        version="0.1.0"
    )

    # Setup CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Initialize database
    # init_db_pool()

    # Include API routers
    app.include_router(request_inspect.router, tags=["Request Inspect"])
    app.include_router(status_codes.router, tags=["Status Codes"])
    app.include_router(auth_routes.router, tags=["Auth"])
    app.include_router(response_format.router, tags=["Response formats"])
    app.include_router(dynamic_data.router, tags=["Dynamic Data"])
    app.include_router(redirect.router, tags=["Redirect"])
    app.include_router(anything.router, tags=["Anything"])
    app.include_router(users.router, tags=["Users"])
    app.include_router(posts.router, tags=["Posts"])
    return app


app = create_app()


# Generate new mock data on startup
mock_data = generate_all_mock_data()


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI HTTP Test Service!"}


@app.get("/refresh-data")
def refresh_data():
    global mock_data
    mock_data = generate_all_mock_data()
    return {"message": "Mock data refreshed successfully"}
