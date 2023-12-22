import json
from django.http import JsonResponse
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


class RegisterView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            user = User.objects.create_user(
                username=data["username"],
                password=data["password"],
                email=data["email"],
                first_name=data["first_name"],
                last_name=data["last_name"]
            )
            if (data["is_admin"]):
                user.is_superuser = True
                user.save()
        except Exception as e:
            return JsonResponse({"error": f"{e}"}, status=404)
        return JsonResponse({"data": f"{user.pk}"}, status=201)


class LoginView(View):
    def post(self, request):
        data = json.loads(request.body)
        print(request)
        print(data["username"], data["password"])
        user = authenticate(
            request, username=data["username"], password=data["password"])
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return JsonResponse({'token': token.key})
        else:
            return JsonResponse({'error': 'Invalid Credentials'}, status=401)
