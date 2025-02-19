import firebase_admin.auth as auth
from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse
from django.contrib.auth.models import User

class AuthUser:
    def __init__(self, data):
        self.first_name = data.get('first_name')
        self.last_name = data.get('last_name')
        self.username = data.get('username')

class FirebaseAuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        auth_header = request.META.get("HTTP_AUTHORIZATION", None)
        if auth_header:
            try:
                token = auth_header.split(" ")[1]
                decoded_token = auth.verify_id_token(token)
                request.user = User(decoded_token)
            except Exception as e:
                return JsonResponse({"error": "Invalid authentication token."}, status=401)
        else:
            user = None
            request.user = AuthUser(user)