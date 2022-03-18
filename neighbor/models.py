from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Neighborhood(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    total_occupants = models.IntegerField()
    neighborhood_logo = models.ImageField(upload_to='images/')
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    health_contacts = models.CharField(max_length=50)
    police_contacts = models.CharField(max_length=50)

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    def update_neighborhood(self):
        self.save()

    def update_total_occupants(self):
        self.save()

    @classmethod
    def get_neighborhood_by_user(cls, user):
        neighborhood = cls.objects.filter(user=user)
        return neighborhood


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    username = models.CharField(max_length=100)
    profile_photo = models.ImageField(upload_to='posts/')
    national_id = models.CharField(max_length=9)
    neighborhood = models.ForeignKey(
        Neighborhood, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_profile(self,):
        self.save()

    @classmethod
    def get_profile_by_user(cls, user):
        profile = cls.objects.filter(user=user)
        return profile

class Business(models.Model):
    business_name = models.CharField(max_length = 100)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    business_photo = models.ImageField(upload_to = 'posts/')
    neighborhood = models.ForeignKey(Neighborhood, on_delete = models.CASCADE)
    business_email = models.CharField(max_length = 100)

    def create_business(self):
        self.save()

    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    def update_business(self):
        self.save()

    @classmethod
    def get_business(cls):
        business = cls.objects.all()
        return business

    @classmethod
    def get_business_by_user(cls, user):
        business = cls.objects.filter(user=user)
        return business

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    pub_date = models.DateTimeField(auto_now_add=True)
    post_image = models.ImageField(upload_to = 'posts/')
    caption = models.CharField(max_length=150)
    
    def __str__(self):
        return self.post

    def save_post(self):
        self.save()

    @classmethod
    def get_posts(cls):
        posts = cls.objects.all()
        return posts
