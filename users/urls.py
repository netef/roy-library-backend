from django.urls import path
from . import views

urlpatterns = [
    path("", views.UsersView.as_view()),
    path("<int:pk>", views.UsersModifyView.as_view())
]
