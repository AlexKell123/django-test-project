from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_all_posts, name='show_all_posts'),
    path('post/<int:pk>/', views.current_post, name='current_post'),
    path('post/new/', views.new_post, name='new_post'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('profile/id<int:user_id>', views.show_profile, name='profile'),
    path('profile/id<int:user_id>/posts', views.show_profile_posts, name='profile_posts'),
    path('profile/new', views.register, name='register'),
]
