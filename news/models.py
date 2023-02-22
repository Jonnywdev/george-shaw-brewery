from django.db import models
from profiles.models import UserProfile
# Create your models here.


class RecentNews(models.Model):
    title = models.CharField(max_length=225)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    body = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title + ' | ' + self.author
