from django.urls import path

from . import views
app_name = 'post'

urlpatterns=[
    path('', views.index, name='index'), # List
    path('create/', views.post_create),
    path('<int:pk>/', views.post_receive, name='detail'),
    path('update/<int:pk>/', views.post_update),
]