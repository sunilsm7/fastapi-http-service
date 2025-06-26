# FASTAPI HTTP Request & Response Test Service
A fully featured HTTP Request & Response service inspired by [httpbin.org](https://httpbin.org/#/), built using **FastAPI**.

HTTP Request & Response Test Service using FastAPI, with support for:

- Auth (Basic, Bearer, Digest, JWT)
- Request/Response inspection
- Status simulation
- Encoding (gzip, deflate, etc.)
- Cookies, redirects, image serving, etc.

## Installation

```bash
# 1. Clone the repo
$ git clone <repo_url>

$ cd fastapi-http-service

# 2. Install dependencies
$ pip install -r requirements.txt

# 3. Run the app
$ uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```


##  API Docs

FastAPI provides Swagger and ReDoc automatically:

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---
