from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        # Returns the URL to this post's detail page (e.g., /post/1/)
        # Uses Django's reverse() to find the URL by its name in urls.py
        return reverse('post-detail', args={str(self.id)})
    
