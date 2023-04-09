from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title