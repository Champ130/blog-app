from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default/jpg',upload_to='profile_pics')



    def __str__(self):
        return f'{self.user.username} profile'
    
    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'pk': self.pk})


# class Addblog(models.Model):
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     date_posted = models.DateField(default=timezone.now)
#     def __str__(self):
#         return self.title
#     class meta:
#         db_table='addblog'