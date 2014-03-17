from django.db import models
from django.contrib.auth.models import User

'''esta clase nos sivre para extender el modelo de usuario
 de django'''
class userProfile(models.Model):
    user = models.OneToOneField(User)
