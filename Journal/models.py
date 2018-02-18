from django.db import models
from django.utils import timezone

class Question(models.Model):
    questionText = models.CharField(max_length = 200)
    publishDate = models.DateTimeField("Question publish date", null = True)

class Choice(models.Model):
    question = models.ForeignKey("Question", on_delete=models.DO_NOTHING)
    answer = models.CharField(max_length = 200)
    votesCount = models.IntegerField(default=0)

class Post(models.Model):
    title = models.CharField(max_length = 100, null = True)
    postText = models.TextField()
    publishDate = models.DateTimeField(default = timezone.now)
    author = models.CharField(max_length = 35, null = True)

