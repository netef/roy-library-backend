from django.http import HttpResponse
from django.views.generic import View
# Create your views here.


class BooksView(View):
    def post(self, request):
        return HttpResponse("Book created.")

    def get(self, request):
        return HttpResponse("Books list.")

    def put(self, request):
        return HttpResponse("Books changed.")

    def delete(self, request):
        return HttpResponse("Book deleted.")
