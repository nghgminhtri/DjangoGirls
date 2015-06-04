from django.db import models
from django.utils import timezone
from django.contrib.auth.decorators import login_required

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    def unpublish(self):
        self.published_date = None
        self.save()
    
    def approved_comments(self):
        return self.comments.filter(approved=True)
    
    def unapproved_comments(self):
        return self.comments.filter(approved=False)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default=False)

    def approve(self):
        self.approved = True
        self.save()
    
    def unapprove(self):
        self.approved = False
        self.save()

    def __str__(self):
        return self.text