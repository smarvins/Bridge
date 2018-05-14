from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class app(models.Model):
    thumb = models.ImageField(default= 'default.png', blank=True)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # nickname = models.ForeignKey(User, default=None)

    def __str__(self):
        return self.body

class profile(models.Model):
    name = models.TextField()
    profilepic = models.ImageField(default= 'default.png', blank=True)
    backgroundimage = models.ImageField(default= 'default.png', blank=True)
    bio = models.TextField()
    email = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # nickname = models.ForeignKey(User)

    def __str__(self):
        return self.name
