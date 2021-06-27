from django.urls import path
from blog.views import ListPost, PostDetail, PostCreate

urlpatterns = [
    path('', ListPost.as_view(), name='post_list'),
    path('post/<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('post/create', PostCreate.as_view(), name='post_create'),
]