from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.conf import settings
from piesbook_test.settings import MEDIA_URL, MEDIA_ROOT




class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.FileField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(
        auto_now_add=True, null=True)

    def get_absolute_url(self):
        return reverse('forum:post_detail',kwargs={'pk':self.pk})



    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# class Pet(models.Model):
#     Name = models.CharField(max_length=200)
#     Type =

