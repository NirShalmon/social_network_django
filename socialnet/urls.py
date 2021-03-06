from django.urls import path, reverse_lazy
from .views import *
from django.views.generic import TemplateView, RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url=reverse_lazy('about')), name='home'),
    path('posts/', PostListView.as_view(), name='posts'),
    path('new_post/', PostCreateView.as_view(), name='new post'),
    path('like_list/', LikeListView.as_view(), name='likes'),
    path('like/', LikeView.as_view(), name='like'),
    path('unlike/', UnlikeView.as_view(), name='unlike'),
    path('comment/', CommentView.as_view(), name='comment'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
]
