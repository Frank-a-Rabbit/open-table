from django.http import JsonResponse
from django.shortcuts import redirect
from django.views import View


class HomePageView(View):
    def get(self, request):
        print('Testing')

        # Check if the user is authenticated
        if request.user.is_authenticated:
            return JsonResponse({"message": "Welcome!", "user": request.user.username})
        else:
            return JsonResponse({"error": "Unauthorized"}, status=401)
