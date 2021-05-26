from django.urls import path
from .views import PostList, PostDetail, CreatePost, AdminPostDetail

app_name = 'meme'

urlpatterns = [
    path('memes/', PostList.as_view(), name='listpost'),
    path('meme/<int:pk>/', PostDetail.as_view(), name='detailpost'),
    path('create/', CreatePost.as_view(), name='createpost'),
    path('meme/admin/<int:pk>/', AdminPostDetail.as_view(), name='admindetailpost'),
]