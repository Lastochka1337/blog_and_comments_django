from django.db import models

class Post(models.Model):
    name = models.CharField(max_length = 100)
    content = models.TextField()
    publication_date = models.DateField()
    comments = models.ManyToManyField("Commentary")

    def __str__(self):
        return self.name

class Commentary(models.Model):
    text = models.TextField()
    author = models.CharField(max_length = 100)
    creation_date = models.DateField()

    def __str__(self):
        return self.name