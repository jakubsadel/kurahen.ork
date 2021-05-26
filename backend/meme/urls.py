from django.urls import path
from .views import PostList, PostDetail, CreatePost, DeletePost, EditPost

app_name = 'meme'

urlpatterns = [
    path('memes', PostList.as_view(), name='listpost'),
    path('meme/<int:pk>/', PostDetail.as_view(), name='detailpost'),
    path('create/', CreatePost.as_view(), name='createpost'),
    path('admin/edit/<int:pk>/', EditPost.as_view(), name='editpost'),
    path('admin/delete/<int:pk>/', DeletePost.as_view(), name='deletepost'),
]