from django.db import models

# Create your models here.
class BlogPosts(models.Model):
    url = models.CharField(max_length=250)
    txt = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.txt}"