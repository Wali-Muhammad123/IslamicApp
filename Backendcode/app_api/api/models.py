from django.db import models

# Create your models here.
class Announcements(models.Model):
    date=models.DateField()
    title=models.CharField(max_length=100)
    announcement=models.TextField()
    def __str__(self):
        return self.title
class prayer(models.Model):
    time=models.TimeField()
    prayer=models.CharField(max_length=15)
    def __str__(self):
        return self.prayer