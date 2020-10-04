""" formulario de los usuarios """

#django
from django import forms
from django.contrib.auth.models import User

#model
from users.models import Profile

#VALIDACIONES DE LOS FORMULARIOS DE LOS USUARIOS

class ProfileForm(forms.Form):

    website = forms.URLField(max_length= 200 , required= False)
    biography = forms.CharField(max_length= 500 , required= False)
    phone_number = forms.CharField(max_length= 20 , required= False)
    picture = forms.ImageField(required= True)


class SignupForm(forms.Form):

    username = forms.CharField(min_length= 4 ,max_length=50)
    password = forms.CharField(max_length= 70 , widget= forms.PasswordInput())
    password_confirmation = forms.CharField(max_length= 70 , widget= forms.PasswordInput())

    first_name = forms.CharField(max_length=50 , min_length= 4)
    last_name = forms.CharField(max_length=50 , min_length= 4)

    email = forms.CharField(min_length=6 , max_length= 70 , widget=forms.EmailInput())


    def clean_username(self):
        """para que el username sea único"""

        username = self.cleaned_data['username']

        username_exist = User.objects.filter(username = username).exists()

        if username_exist:

            raise forms.ValidationError('Username is already in use')
        
        #SIEMPRE HAY QUE REGRESAR EL CAMPO 
        return username

    def clean(self):
        """Verificamos si la password coninside con el passwordconfirmation """

        data = super().clean()#como estamos escribiendo el método clean (es un método que trae django por defecto)
                              #Usamos "super()" para llamar al método como estaba antes
        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:

            raise forms.ValidationError('Passwords do not match')

        #SIEMPRE HAY QUE REGRESAR EL CAMPO 
        return data


    def save(self):
        """guardar lo del formulario"""

        data = self.cleaned_data
        data.pop('password_confirmation')#no hace falta guardar la confirmación de la contraseña

        user = User.objects.create_user(**data)
        
        profile = Profile(user = user)

        profile.save()