from django.db import models

# Create your models here.
class Team(models.Model):

    profile_pic = models.ImageField(upload_to='teams/pics/%Y/%m/%d/')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    facebook_link = models.URLField(max_length=100)
    twitter_link =models.URLField(max_length=100)
    google_plus_link =models.URLField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __STR__(self):
        return self.first_name