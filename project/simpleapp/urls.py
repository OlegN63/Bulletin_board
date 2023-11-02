from django.urls import path
from .views import PostList, PostDetail, PostCreate, PostUpdate, PostDelete, CommentCreate
from django.contrib.auth.views import LoginView, LogoutView
from .views import BaseRegisterView
from . import views

urlpatterns = [
    path('', PostList.as_view(), name='posts'),
    path('<int:pk>/', PostDetail.as_view(), name='post'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('signup/', BaseRegisterView.as_view(template_name='signup.html'), name='signup'),
    path('<int:pk>/create_comment/', CommentCreate.as_view(), name='comment_create'),
    path('private_comment/', views.private_comment, name='private_comment'),
]