from django.db import models
from django.utils import timezone
# from django.core.urlresolevers import revers

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    # image = models.FileField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# class Pet(models.Model):
#     Name = models.CharField(max_length=200)
#     Type =

