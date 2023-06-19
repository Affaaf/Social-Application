from django.db import models
from user_authentication_app.models import User

# Create your models here.

class Post(models.Model):
    post_text = models.TextField( max_length=250)
    created_at = models.DateField( auto_now_add=True, blank=True , null=True)
    like = models.IntegerField( null=True, blank=True, default=0)
    user = models.ForeignKey(User, on_delete = models.CASCADE,related_name ='post_user_related_name',null=True, blank=True)
    
    def __str__(self):
        return self.post_text

class Like(models.Model):
    is_active=models.BooleanField( null=True, blank= True)
    created_at = models.DateField( auto_now_add=True, blank=True , null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_like_related')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_like_related')
    
    def __str__(self):
        return str(self.is_active)