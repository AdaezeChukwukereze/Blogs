from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateField()
    reporter = models.CharField(max_length=15)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "News"