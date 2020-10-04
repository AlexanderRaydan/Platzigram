"""ESTE ARCHIVO SIEMPRE SERÁN LAS URLS"""

#Django
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

from platzigram import views as local_views #vista de la carpeta local de platzigram
from posts import views as posts_views #vistas de la aplicación de post




urlpatterns = [
    path('admin/', admin.site.urls),#primer argumento siempre el la url, el segundo es la vista
    path('hello-word/', local_views.hello_world),
    path('sorted/', local_views.sorted_numbers),
    path('Say_Hi/<str:name>/<int:age>', local_views.sayHi ),
    path('posts/', posts_views.list_posts),
]
