import json
from django.core import exceptions
from django.http import JsonResponse
from django.views import View
from .models import User
from books.models import Book


class UsersView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            user = User(**data)
            user.save()
        except:
            return JsonResponse({"error": "cannot create a new user"}, status=404)
        return JsonResponse({"data": f"{user.pk}"}, status=201)

    def get(self, request):
        try:
            users = User.objects.all()
        except User.DoesNotExist:
            return JsonResponse({'error': 'Users not found'}, status=404)
        users = User.serialize_lst(users)
        return JsonResponse(users, status=200, safe=False)


class UsersModifyView(View):
    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist as e:
            return JsonResponse({'error': f'{e}'}, status=404, safe=False)
        user = User.serialize(user)
        return JsonResponse(user, status=200)

    def patch(self, request, pk):
        try:
            user = User.objects.filter(pk=pk)
            if user.count() == 0:
                raise exceptions.EmptyResultSet(f"Unable to find user {pk}")
            data = json.loads(request.body)
            user.update(**data)
        except exceptions.FieldDoesNotExist as e:
            return JsonResponse({'error': f'{e}'}, status=404)
        except exceptions.EmptyResultSet as e:
            return JsonResponse({'error': f'{e}'}, status=404)
        return JsonResponse({"data": f"User {pk} changed."}, status=203,)

    def delete(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
            user.delete()
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
        return JsonResponse({"data": f"User {pk} deleted."})
