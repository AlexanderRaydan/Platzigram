"""ESTE ARCHIVO SIEMPRE SERÁN LAS URLS"""

#Django
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.http import HttpResponse
from django.conf.urls.static import static #para las imágenes

#local
from posts import views as posts_views
from users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls , name = 'admin'),#primer argumento siempre el la url, el segundo es la vista

    path('posts/', posts_views.list_posts , name = 'feed'),
    path('posts/new/', posts_views.create_post , name = 'create_post'),
    path('posts/<str:post_id>/', posts_views.Post_detail_view, name = 'post_detail' ),


    path('users/login/', users_views.login_view, name = 'login' ),
    path('users/logout/', users_views.logout_view, name = 'logout' ),
    path('users/signup/', users_views.signup, name = 'signup' ),
    path('users/me/profile', users_views.update_profile, name = 'update_profile' ),    
    path('users/<str:username>/', users_views.user_details, name = 'user_detail' ),
    path('users/follow/<str:user_to_id>/', users_views.user_follow_view, name = 'user_follow' ),
    path('users/unfollow/<str:user_to_id>/', users_views.user_unfollow_view, name = 'user_unfollow' ),




    #path('', include(('posts.urls', 'posts'), namespace='posts')),
    #path('users/', include(('users.urls', 'users'), namespace='users')),

] + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT) # para las imágenes
