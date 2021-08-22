from django.db import models

# Create your models here.
# model ------> excel sheet (table)

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=13)
    slug = models.CharField(max_length=130)
    timeStamp = models.TimeField(blank=False)
    DateStamp = models.DateField(blank=False)

    def __str__(self):
        return self.title + ' by ' + self.author