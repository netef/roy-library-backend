from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def get_books(request):
    return HttpResponse("Books list.")


def create_book(request):
    return HttpResponse("Book created.")
