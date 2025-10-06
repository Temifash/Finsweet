from django.db import models

# Create your models here.
class NewBlog(models.Model):
    title = models.CharField(max_length=225)
    description = models.CharField(max_length=250)
    content = models.TextField()
    image = models.ImageField(default='sample.png', blank=True)

    def __str__(self):
        return f'{self.title}'