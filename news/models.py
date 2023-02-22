from django.db import models

# Create your models here.


class RecentNews(models.Model):

    title = models.CharField(max_length=200)
    body = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title
