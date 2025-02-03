from django.http import HttpResponse
from django.shortcuts import redirect
from django.views import View


class HomePageView(View):
    def get(self, request):
        if request.user:
            return HttpResponse(f"Welcome, {request.user.username}!")
        else:
            print('No authenticated user')
            return redirect('/login/')