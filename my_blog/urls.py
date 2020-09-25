from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:post_pk>/detail', views.post_detail, name='post_detail'),
    path('post/<int:post_pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:post_pk>/delete', views.post_delete, name='post_delete'),
    path('draft/list/', views.post_draft_list, name='post_draft_list'),
    path('post/<int:post_pk>/publish/', views.post_publish, name='post_publish'),


]