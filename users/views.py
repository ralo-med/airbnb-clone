from django.views import View
from django.shortcuts import render


# Create your views here.
class LoginView(View):
    def get(self, request):
        return render(request, "users/login.html")

    def post(self, request):
        pass


"""
def login_view(request):
    if request.method =="GET":
        pass
    if request.method =="POST:
        pass
"""
