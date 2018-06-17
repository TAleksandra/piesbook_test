from django.db import models
from django.utils import timezone
from django.urls import reverse




class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.CharField(max_length=100000)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

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

