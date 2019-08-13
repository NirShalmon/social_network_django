from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, HttpResponseBadRequest
from django.views.generic.base import View
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render

from .models import *
from .forms import *


class PostListView(LoginRequiredMixin, View):
    def get(self, request):
        posts_to_show = Post.objects.order_by('-pub_time')
        is_liked = [post.likes.filter(pk=request.user.pk).exists() for post in posts_to_show]
        context = {
            'post_list': zip(posts_to_show, is_liked),
            'user': self.request.user
        }
        return render(self.request, 'post_list.html', context)


class LikeListView(ListView):
    template_name = 'like_list.html'
    model = get_user_model()
    ordering = ['username']

    def get_queryset(self):
        if 'post_id' in self.request.GET:
            get_object_or_404(Post, pk=self.request.GET['post_id'])
            return get_user_model().objects.filter(socialnet_post_likes=self.request.GET['post_id'])
        elif 'comment_id' in self.request.GET:
            get_object_or_404(Comment, pk=self.request.GET['comment_id'])
            return get_user_model().objects.filter(socialnet_comment_likes=self.request.GET['comment_id'])
        return get_user_model().objects.none()


class LikeView(LoginRequiredMixin, View):
    def post(self, request):
        if 'post_id' in request.POST:
            post = get_object_or_404(Post, pk=request.POST['post_id'])
            self.request.user.socialnet_post_like_set.add(post)
        elif 'comment_id' in request.POST:
            comment = get_object_or_404(Comment, pk=request.POST['comment_id'])
            self.request.user.socialnet_comment_like_set.add(comment)
        else:
            return HttpResponseNotFound()
        return HttpResponse()


class CommentView(LoginRequiredMixin, View):
    def post(self, request):
        if 'post_id' in request.POST:
            parent_content = get_object_or_404(Post, pk=request.POST['post_id'])
        elif 'comment_id' in request.POST:
            parent_content = get_object_or_404(Comment, pk=request.POST['comment_id'])
        else:
            return HttpResponseNotFound()
        comment_text =  request.POST.get('comment', '').strip()
        if not comment_text:
            return HttpResponseBadRequest()
        comment = Comment(author=request.user, text=comment_text, parent_content=parent_content)
        comment.save()
        return HttpResponseRedirect(reverse_lazy('posts'))


class UnlikeView(LoginRequiredMixin, View):
    def post(self, request):
        if 'post_id' in request.POST:
            post = get_object_or_404(Post, pk=request.POST['post_id'])
            self.request.user.socialnet_post_like_set.remove(post)
        elif 'comment_id' in request.POST:
            comment = get_object_or_404(Comment, pk=request.POST['comment_id'])
            self.request.user.socialnet_comment_list_set.remove(comment)
        else:
            return HttpResponseNotFound()
        return HttpResponse()



class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'new_post.html'
    model = Post
    form_class = NewPostForm
    success_url = reverse_lazy('posts')

    def dispatch(self, *args, **kwargs):
        return super(PostCreateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return HttpResponseRedirect(self.success_url)
