from django.db import models


class News(models.Model):

    class Meta:
        verbose_name_plural = 'News'
        ordering = ["-created_on"]

    title = models.CharField(max_length=254)
    content = models.TextField()
    img_url = models.URLField(max_length=1024, null=True, blank=True)
    img = models.ImageField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.title