from django.core import exceptions
from django.http import JsonResponse
from django.views import View
import json
from .models import Book


class BooksView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            book = Book(**data)
            book.save()
        except:
            return JsonResponse({"error": "cannot create a new book"}, status=404)
        return JsonResponse({"data": f"{book.pk}"}, status=201)

    def get(self, request):
        try:
            books = Book.objects.all()
        except Book.DoesNotExist:
            return JsonResponse({'error': 'Books not found'}, status=404)
        books = Book.serialize_lst(books)
        return JsonResponse(books, status=200, safe=False)


class BooksModifyView(View):
    def get(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist as e:
            return JsonResponse({'error': f'{e}'}, status=404, safe=False)
        book = Book.serialize(book)
        return JsonResponse(book, status=200)

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
            return JsonResponse({'error': 'Book not found'}, status=404)
        return JsonResponse({"data": f"Book {pk} deleted."})
