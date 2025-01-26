from django.urls import path
from ..views import UserDetailAPIView

urlpatterns = [
    path('users/<uuid:uid>/', UserDetailAPIView.as_view(), name='user-detail'),
]