from django.urls import path
from .views import *

urlpatterns = [
    path('posts/', PostListView.as_view(), name='posts'),
    path('new_post/', PostCreateView.as_view(), name='new post'),
]