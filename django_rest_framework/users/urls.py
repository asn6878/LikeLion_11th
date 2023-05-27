from django.urls import path, include

from .views import *

urlpatterns = [
    path('',SignUpView.as_view(), name='register'),
    path('<int:pk>/',DetailView.as_view()),
]
