from django.urls import path
from . import views
from user import views as user_views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('favourite_posts/', views.favourite_posts, name='favourite_posts'),
    path('create_user/', user_views.create_user, name='create_user'),
    path('login/', user_views.user_login, name='login'),
    path('logout/', user_views.user_logout, name='logout'),
    path('profile/', user_views.user_profile, name='user_profile'),
    path('post/create/', views.post_create, name='post_create'),
    path('favourite/', views.favourite, name='favourite'),
    path('post/<int:pk>/<slug:slug>/', views.post_detail, name='post_detail'),
    path('like_post/', views.like_post, name='like_post'),
    path('post/<int:pk>/<slug:slug>/edit', views.post_edit, name='post_edit'),
    path('pdf/<int:pk>/<int:post_pk>/delete/', views.pdf_delete, name='pdf_delete'),
    path('image/<int:image_pk>/<int:post_pk>/delete/', views.delete_image, name='delete_image'),
    path('image/<int:image_pk>/<int:post_pk>/edit/', views.edit_image, name='edit_image'),
    path('image/<int:post_pk>/add/', views.add_image, name='add_image'),
    path('images_album/', views.images_album, name='images_album'),
    path('pdf/<int:post_pk>/add/', views.add_post_pdf, name='add_pdf'),
    path('post_pdf_list/', views.post_pdf_list, name='post_pdf_list'),
    path('pdf_list/', views.pdf_list, name='pdf_list'),
    path('upload_pdf/', views.upload_pdf, name='upload_pdf'),
    path('my-books/', views.my_books, name='my_books'),
    path('add-to-my-books/<int:pk>/', views.add_to_my_books, name='add_to_my_books'),
    path('remove-from-my-books/<int:pk>/', views.remove_from_my_books, name='remove_from_my_books')
]
