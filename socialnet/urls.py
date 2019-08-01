from django.urls import path
from .views import *

urlpatterns = [
    path('posts/', PostListView.as_view(), name='posts'),
    path('new_post/', PostCreateView.as_view(), name='new post'),
    path('like_list/', LikeListView.as_view(), name='likes'),
    path('like/', LikeView.as_view(), name='like'),
    path('unlike/', UnlikeView.as_view(), name='unlike'),
]
