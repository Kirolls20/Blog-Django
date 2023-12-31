from django.db import models
from django.contrib.auth.models import AbstractUser,User
from .core import TimeStampedModel


class CustomModelManager(models.Manager):
    
    def active_users(self):
        return self.filter(is_active=True).count()
    
class User(AbstractUser):
    profile_img = models.ImageField(null= True,blank=True,upload_to='profile_images/')
    follows = models.ManyToManyField(
        'self',
        related_name='followed_by',
        symmetrical=False,
        blank =True
    )
    profile_create = models.DateTimeField(auto_now_add=True)
    profile_update= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
    
    objects = CustomModelManager()

class Blog(TimeStampedModel):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    title= models.CharField(max_length=200,blank=False)
    blog_body = models.TextField()
    blog_img = models.ImageField(blank=True,null=True,upload_to='blog_imgs/')
    likes = models.ManyToManyField(User,related_name='blog_likes',blank=True)
    comments = models.ManyToManyField(User,related_name='blog_comments',through='Comment')
    

    # created_date = models.DateTimeField(auto_now_add=True)
    # updated_date = models.DateTimeField(auto_now=True)

    def total_likes(self):
        return self.likes.count()
    
    def total_comments(self):
        return self.comments.count()
    
    def __str__(self):
        return self.title 
    

class Comment(TimeStampedModel):    
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.TextField()
    
    # comment_created= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment
    

    

