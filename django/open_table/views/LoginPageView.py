from django.contrib.auth import login
from django.http import JsonResponse
from django.views import View
from firebase_admin import auth
from django.contrib.auth.models import User

class UserAuthenticationView(View):
    def post(self, request):
        """Handles user login or creation based on Firebase token."""
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return JsonResponse({"error": "No authentication token provided."}, status=401)

        try:
            token = auth_header.split(" ")[1]  # Extract the ID token
            decoded_token = auth.verify_id_token(token)
            uid = decoded_token.get("uid")  # Firebase UID
            email = decoded_token.get("email")

            # Retrieve or create a user in Django's database
            user = User.objects.get_or_create(username=uid, email=email)

            # Log the user into Django
            login(request, user)
            return JsonResponse({"message": "User logged in successfully!"})

        except Exception as e:
            return JsonResponse({"error": "Invalid authentication token."}, status=401)