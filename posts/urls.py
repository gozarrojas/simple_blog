from django.urls import path
from posts.views import *

app_name = 'posts'

urlpatterns = [
    path('', PostsFeedView.as_view(), name='blog'),
    path('posts/add/', AddPostView.as_view(), name='add_post'),
    path('posts/edit/<int:pk>',UpdatePostView.as_view(),name='edit_post'),
    path('posts/remove/<int:pk>/', DeletePostView.as_view(), name='delete_post'),
    path('posts/detail/<slug:url>/', PostDetailView.as_view(), name='detail'),
    path('posts/save_comment', save_comment, name='save_comment'),

]
