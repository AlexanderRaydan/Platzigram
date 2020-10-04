#django
from django.shortcuts import redirect
from django.urls import reverse

class ProfileCompletionMiddleware:
    """ Esto obliga al todos los usuarios
    de tener un firt_name para poder acceder al perfil"""

    def __init__ (self , get_response):

        self.get_response = get_response

    def __call__ (self, request):

        if not request.user.is_anonymous:

            if not request.user.is_staff:

                profile = request.user.profile

                if not profile.picture : # si no tine foto de perfil, lo redirige a "update_profile"
                    
                    if request.path not in [reverse('update_profile'), reverse('logout')]:

                        return redirect('update_profile')
        
        reponse = self.get_response(request)
        return reponse
