from rest_framework.urls import path
from . import views


urlpatterns = [
    path('next-question/', views.LoadAPIView.as_view()),
]
