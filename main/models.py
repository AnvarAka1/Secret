from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Tags(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    keywords = models.TextField()

    telegram_url = models.CharField(max_length=128)
    facebook_url = models.CharField(max_length=128)
    twitter_url = models.CharField(max_length=128)
    instagram_url = models.CharField(max_length=128)


class Post(models.Model):
    title = models.CharField(max_length=128)
    image = models.ImageField(upload_to='images')
    content = RichTextUploadingField()


class Gallery(models.Model):
    post = models.ForeignKey(Post)
    image = models.ImageField(upload_to='images')
