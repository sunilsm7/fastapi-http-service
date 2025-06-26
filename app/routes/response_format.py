from fastapi import APIRouter, Response
import gzip
import brotli
import zlib

router = APIRouter()


@router.get("/encoding/utf8")
def utf8():
    return Response(content="\u2713 UTF-8 content!", media_type="text/plain; charset=utf-8")


@router.get("/gzip")
def gzip_encoded():
    data = gzip.compress(b"Gzipped content")
    return Response(content=data, media_type="application/gzip")


@router.get("/deflate")
def deflate_encoded():
    data = zlib.compress(b"Deflated content")
    return Response(content=data, media_type="application/zlib")


@router.get("/brotli")
def brotli_encoded():
    data = brotli.compress(b"Brotli content")
    return Response(content=data, media_type="application/x-brotli")


@router.get("/html")
def html():
    return Response(content="<html><body><h1>Sample HTML</h1></body></html>", media_type="text/html")


@router.get("/json")
def json():
    return {"message": "Hello, JSON!"}


@router.get("/xml")
def xml():
    return Response(content="<message>Hello, XML!</message>", media_type="application/xml")


@router.get("/robots.txt")
def robots():
    return Response(content="User-agent: *\nDisallow: /deny", media_type="text/plain")


@router.get("/deny")
def deny():
    return Response(content="Access denied by robots.txt rules", status_code=403)
