from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    profile_pic = models.ImageField(upload_to='profile-images/', default='DEFAULT VALUE')
    bio = models.TextField(max_length=500, default="My Bio", blank=True)

    def __str__(self):
        return f'{self.user.username} Profile Details'

    def save_profile(self):
      self.save()

    def delete_profile(self):
      self.delete()


class Post(models.Model):
  image = models.ImageField(upload_to = 'post-images/',default='DEFAULT VALUE')
  caption = models.TextField()
  #Create a foreign key column that will store the ID of the Profile from the Profile table
  user = models.ForeignKey(Profile,on_delete=models.CASCADE)
  #Automatically save the exact time and date to the database as soon as we save the model.
  date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
        return self.caption

  def save_post(self):
    self.save()

  def delete_post (self):
    self.delete()
