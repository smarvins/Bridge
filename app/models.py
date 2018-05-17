from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class app(models.Model):
    thumb = models.ImageField(default= 'default.png', blank=True)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    nickname = models.ForeignKey(User, null=True)

    def __str__(self):
        return self.body

class profile(models.Model):
    name = models.TextField()
    profilepic = models.ImageField(default= 'default.png', blank=True)
    backgroundimage = models.ImageField(default= 'default.png', blank=True)
    bio = models.TextField()
    email = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    nickname = models.ForeignKey(User, null=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
  nickname = models.ForeignKey(User, null=True)
  comment = models.CharField(max_length = 100)
  post_on = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.comment



# class Like(models.Model):
#   nickname = models.ForeignKey(User, null=True)
#   def __str__(self):
#     return 'Like:' + self.nickname+ ' ' + self.post.title
