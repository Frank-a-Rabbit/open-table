from django.http import HttpResponse
from django.shortcuts import redirect
from django.views import View


class HomePageView(View):
    def get(self, request):
        print('Testing')
        # Check if the user is authenticated
        if request.user.is_authenticated:
            return HttpResponse(f"Welcome, {request.user.username}!")
        else:
            return redirect('/login/')  # Redirect to login page if not authenticated