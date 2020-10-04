#django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

#Models
from users.models import Profile
from users.models import Contact
from posts.models import Post
import posts

@admin.register(Profile)#registramos nuestro modelo de "Profile" en el sitio de admin
class ProfileAdmin(admin.ModelAdmin):

    list_display = ('pk','user' , 'phone_number' , 'website' , 'picture') #como quiero que se listen las cosas en el admin
    list_display_links = ('user' , 'pk')
    list_editable = ('phone_number' , 'picture' , )
    search_fields = (   #busqueda
        'user__email', 
        'user_username',
        'user__firt_name' ,
        'user__last_name',
        'user__phone_number'
        )
    
    list_filter = ('created' , 'modified' , 'user__is_active' , 'user__is_staff') #filtros


    fieldsets = (
        ('Profile',{
            'fields':(('user','picture'),)
        }),
        ('Extra info',{
            'fields':(
                ('website','phone_number'),
                ('biography'),
            )
        }),
        ('Metadata',{
            'fields':(('created','modified'),),
        })
    )
    readonly_fields = ('created','modified')


"""
Une los modelos de usuario y perfil para no tener que crear un usuario para asociarlo con un perfil
"""
class ProfileInLine(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInLine, )
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )


@admin.register(Post)#registramos nuestro modelo de "Profile" en el sitio de admin
class PostsAdmin(admin.ModelAdmin):

    list_display = ('pk','user' , 'title', 'photo') #como quiero que se listen las cosas en el admin
    

@admin.register(Contact)#registramos nuestro modelo de "Profile" en el sitio de admin
class ContactAdmin(admin.ModelAdmin):

    list_display = ('user_from','user_to' , 'created')
    

admin.site.unregister(User)
admin.site.register(User,UserAdmin)