from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from django.urls import reverse_lazy
from .filters import PostFilter
from .forms import PostForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .models import BaseRegisterForm
from django.core.mail import EmailMessage

# Create your views here.

class PostList(LoginRequiredMixin, ListView):
    model = Post
    ordering = "header"
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 3


    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostDetail(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
    queryset = Post.objects.all()

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_create.html'
    context_object_name = 'post_create'
    form_class = PostForm

class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'post_update.html'
    context_object_name = 'post_update'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts')
    context_object_name = 'post_delete'

class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'

class CommentCreate(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'comment_create.html'
    context_object_name = 'comment_create'
    form_class = CommentForm

@login_required
def private_comment(request):
    user = request.user
    user_posts = user.post_set.all()
    selected_post_id = request.GET.get('post')

    comments = Comment.objects.filter(post__author=user)
    if selected_post_id:
        comments = comments.filter(post__id=selected_post_id)

    if request.method == 'GET':
        selected_post_id = request.GET.get('post')
        if selected_post_id:
            comments = comments.filter(post__id=selected_post_id)

    return render(request, 'private_comment.html', {'comments': comments, 'user_posts': user_posts, 'selected_post_id': selected_post_id})
