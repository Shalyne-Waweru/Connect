import re
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    profile_pic = models.ImageField(upload_to='profile-images/', default='static/images/default.png')
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile Details'

    def save_profile(self):
      self.save()

    def delete_profile(self):
      self.delete()

    @classmethod
    def get_profile(cls, id):
      profile = cls.objects.get(id=id)
      return profile

    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()


class Post(models.Model):
  image = models.ImageField(upload_to = 'post-images/',default='DEFAULT VALUE')
  caption = models.TextField()
  #Create a foreign key column that will store the ID of the User from the User table
  user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')
  #Automatically save the exact time and date to the database as soon as we save the model.
  date = models.DateTimeField(auto_now_add=True)

  class Meta:
        ordering = ["-pk"]

  def __str__(self):
        return self.caption

  def save_post(self):
    self.save()

  def delete_post (self):
    self.delete()

  @classmethod
  def all_posts(cls):
    return cls.objects.all()

