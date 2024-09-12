# """
# URL configuration for rest project.

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/5.1/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path
# from ninja import NinjaAPI, Schema
# from typing import *

# api = NinjaAPI()

# BOOKS = [
#     {"id": 1, "title": "Book 1", "author": "Author 1"},
#     {"id": 2, "title": "Book 2", "author": "Author 2"},
#     {"id": 3, "title": "Book 3", "author": "Author 3"},
# ]

# class BookSchema(Schema):
#     id: int
#     title: str
#     author: str


# @api.get("/books")
# def list_books(request):
#     return BOOKS

# @api.post("/books")
# def create_book(request, book: BookSchema):
#     BOOKS.append(book.__dict__)
#     return BOOKS

# @api.get("/books/{id}")
# def get_book(request, id: int):
#     for book in BOOKS:
#         if book["id"] == id:
#             return book
#     return {"message": "Book not found"}

# @api.patch("/books/{id}")
# def update_book(request, id: int, book: BookSchema):
#     for i in range(len(BOOKS)):
#         if BOOKS[i]["id"] == id:
#             BOOKS[i] = book.__dict__
#             return BOOKS
#     return {"message": "Book not found"}

# @api.delete("/books/{id}")
# def delete_book(request, id: int):
#     for i in range(len(BOOKS)):
#         if BOOKS[i]["id"] == id:
#             BOOKS.pop(i)
#             return BOOKS
#     return {"message": "Book not found"}

# from django.contrib.auth.models import User

# @api.get("/users")
# def list_users(request):
#     users = User.objects.all()
#     return [
#         {
#             "id": user.id,
#             "username": user.username,
#             "email": user.email,
#             "first_name": user.first_name,
#             "last_name": user.last_name,
#             "is_staff": user.is_staff,
#             "is_active": user.is_active,
#             "is_superuser": user.is_superuser,
#             "date_joined": user.date_joined,
#             "last_login": user.last_login,
#             "user_permissions": [{
#                 'name': permission.name,
#                 'codename': permission.codename,
#                 'content_type': permission.content_type.name,
#             } for permission in user.user_permissions.all()],
#             "groups": [{
#                 'name': group.name,
#                 'permissions': [{
                    
#                 }]
#             } for group in user.groups.all()],
#         }
#         for user in users
#     ]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', api.urls),
# ]
"""
URL configuration for rest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI, Schema
from typing import *
from .router import (
    user_router,
)

api = NinjaAPI()

api.add_router(prefix='user/', router=user_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
]

# BOOKS = [
#     {"id": 1, "title": "Book 1", "author": "Author 1"},
#     {"id": 2, "title": "Book 2", "author": "Author 2"},
#     {"id": 3, "title": "Book 3", "author": "Author 3"},
# ]

# class BookSchema(Schema):
#     id: int
#     title: str
#     author: str


# @api.get("/books")
# def list_books(request):
#     return BOOKS

# @api.post("/books")
# def create_book(request, book: BookSchema):
#     BOOKS.append(book.__dict__)
#     return BOOKS

# @api.get("/books/{id}")
# def get_book(request, id: int):
#     for book in BOOKS:
#         if book["id"] == id:
#             return book
#     return {"message": "Book not found"}

# @api.patch("/books/{id}")
# def update_book(request, id: int, book: BookSchema):
#     for i in range(len(BOOKS)):
#         if BOOKS[i]["id"] == id:
#             BOOKS[i] = book.__dict__
#             return BOOKS
#     return {"message": "Book not found"}

# @api.delete("/books/{id}")
# def delete_book(request, id: int):
#     for i in range(len(BOOKS)):
#         if BOOKS[i]["id"] == id:
#             BOOKS.pop(i)
#             return BOOKS
#     return {"message": "Book not found"}

# from django.contrib.auth.models import User

# @api.get("/users")
# def list_users(request):
#     users = User.objects.all()
#     return [
#         {
#             "id": user.id,
#             "username": user.username,
#             "email": user.email,
#             "first_name": user.first_name,
#             "last_name": user.last_name,
#             "is_staff": user.is_staff,
#             "is_active": user.is_active,
#             "is_superuser": user.is_superuser,
#             "date_joined": user.date_joined,
#             "last_login": user.last_login,
#             "user_permissions": [{
#                 'name': permission.name,
#                 'codename': permission.codename,
#                 'content_type': permission.content_type.name,
#             } for permission in user.user_permissions.all()],
#             "groups": [{
#                 'name': group.name,
#                 'permissions': [{
                    
#                 }]
#             } for group in user.groups.all()],
#         }
#         for user in users
#     ]