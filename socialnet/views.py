from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *


class PostListView(ListView):
    template_name = 'post_list.html'
    model = Post
    ordering = ['-pub_time']


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
