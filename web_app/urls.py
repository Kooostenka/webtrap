from django.urls import path
from .views import IndexView, APIView


urlpatterns = [
    path('', IndexView.as_view()),
    path('api/', APIView.as_view()),
]
