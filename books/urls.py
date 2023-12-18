from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_books),
    path("create/", views.create_book)
]
