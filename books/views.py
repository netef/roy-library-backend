from django.core import exceptions
from django.http import HttpResponse, JsonResponse
from django.views import View
import json
from .models import Book


class BooksView(View):
    def post(self, request):
        data = json.loads(request.body)
        book = Book(
            title=data["title"], available_copies=data["available_copies"], img_url=data["img_url"])
        print(book.available_copies)
        book.save()
        print(book.id)
        return HttpResponse("Book created.")

    def get(self, request):
        try:
            books = Book.objects.all()
        except Book.DoesNotExist:
            return JsonResponse({'error': 'Books not found'}, status=404)
        books = [
            {
                "id": book.pk,
                'title': book.title,
                'available_copies': book.available_copies,
                'date_added': book.date_added,
                'img_url': book.img_url,
            } for book in books
        ]
        return JsonResponse(books, status=200, safe=False)


class BooksModifyView(View):
    def get(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist as e:
            return JsonResponse({'error': 'Book not found'}, status=404)
        data = {
            "id": book.pk,
            "title": book.title,
            "available_copies": book.available_copies,
            "date_added": book.date_added,
            "img_url": book.img_url
        }
        return JsonResponse(data, status=200)

    def patch(self, request, pk):
        try:
            book = Book.objects.filter(pk=pk)
            if book.count() == 0:
                raise exceptions.EmptyResultSet(f"Unable to find book {pk}")
            data = json.loads(request.body)
            book.update(**data)
        except exceptions.FieldDoesNotExist as e:
            return JsonResponse({'error': f'{e}'}, status=404)
        except exceptions.EmptyResultSet as e:
            return JsonResponse({'error': f'{e}'}, status=404)
        return JsonResponse({"data": f"Book {pk} changed."}, status=203,)

    def delete(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            book.delete()
        except Book.DoesNotExist:
            return JsonResponse({'error': 'Books not found'}, status=404)
        return JsonResponse({"data": f"Book {pk} deleted."})
