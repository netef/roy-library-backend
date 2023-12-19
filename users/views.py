from django.http import HttpResponse
from django.views import View


class UserView(View):
    def get(self, request):
        return HttpResponse("get user")

    def post(self, request):
        return HttpResponse("create user")

    def put(self, request):
        return HttpResponse("change user")

    def delete(self, request):
        return HttpResponse("delete user")
