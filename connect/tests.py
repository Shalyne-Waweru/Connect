from django.test import TestCase
from .models import Profile,Post
from django.contrib.auth.models import User

class ProfileTestClass(TestCase):
  '''
  Test class that defines test cases for the model behaviours.

  Args:
      unittest.TestCase: TestCase class that helps in creating test cases
  '''

  def setUp(self):
      '''
      Set up method to run before each test cases.
      It defines instructions that will be executed before each test method.
      '''
      self.user = User(username='wangari')
      self.user.save()

      self.new_profile = Profile(user=self.user, profile_pic='media/profile-images/img1.jpg', bio='This is my bio') 

  # FIRST TEST
  def test_instance(self):
      '''
      test_instance test case to test if the object is initialized properly
      '''
      self.assertTrue(isinstance(self.new_profile,Profile))

  # SECOND TEST
  def test_save_profile(self):
      '''
      test_save_profile test case to test if the object is being saved correctly
      '''
      self.new_profile.save_profile()
      profile = Profile.objects.all()
      self.assertTrue(len(profile) > 0)

  # THIRD TEST
  def test_update_profile(self):
      '''
      test_update_profile test case to test if the object is being updated correctly
      '''
      self.new_profile.save_profile()
      self.new_profile.bio = 'This is my new bio'
      self.assertTrue(self.new_profile.bio == 'This is my new bio')

  # FOURTH TEST
  def test_delete_profile(self):
      '''
      test_delete_profile test case to test if the object is being deleted correctly
      '''
      self.new_profile.save_profile()
      self.new_profile.delete_profile()
      self.assertTrue(len(Profile.objects.all()) == 0)


class PostTestClass(TestCase):
  '''
  Test class that defines test cases for the model behaviours.

  Args:
      unittest.TestCase: TestCase class that helps in creating test cases
  '''

  def setUp(self):
      '''
      Set up method to run before each test cases.
      It defines instructions that will be executed before each test method.
      '''

      # Creating and save a new user object
      self.user = User(username='wangari')
      self.user.save()
      
      # Creating and save a new profile object
      self.new_profile = Profile(user = self.user, profile_pic='media/profile-images/img1.jpg', bio='This is my bio')
      self.new_profile.save()

      self.new_post = Post(image='media/post-images/img1.jpg', caption='This is my post caption', user=self.new_profile) 

  # FIFTH TEST
  def test_instance(self):
      '''
      test_instance test case to test if the object is initialized properly
      '''
      self.assertTrue(isinstance(self.new_post,Post))

  # SIXTH TEST
  def test_save_post(self):
      '''
      test_save_post test case to test if the object is being saved correctly
      '''
      self.new_post.save_post()
      posts = Post.objects.all()
      self.assertTrue(len(posts) > 0)

  # SEVENTH TEST
  def test_update_post(self):
      '''
      test_update_post test case to test if the object is being updated correctly
      '''
      self.new_post.save_post()
      self.new_post.caption = 'This is my new caption'
      self.assertTrue(self.new_post.caption == 'This is my new caption')

  # EIGTH TEST
  def test_delete_post(self):
      '''
      test_delete_post test case to test if the object is being deleted correctly
      '''
      self.new_post.save_post()
      self.new_post.delete_post()
      posts = Post.objects.all()
      self.assertTrue(len(posts) == 0)