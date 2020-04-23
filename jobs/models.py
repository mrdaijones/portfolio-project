from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=100,blank=True)
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    url = models.URLField(blank=True)


    def __str__(self):
        return self.summary
