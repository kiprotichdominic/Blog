from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # CASCADE means that when a user is deleted a profile is deleted and when profile is deleted user is not deleled
    image = models.ImageField(default ='default.jpg', upload_to='profile_pics')
    
    
    def __str__(self):
        return f'{self.user.username} Profile'
    