from django.contrib.auth.models import User
from users.models import Contact

Alex = User.objects.filter(username = 'alex')
Paux = User.objects.filter(username = 'Paux')


follow = Contact(user_from = Alex[0] , user_to = Paux[0])