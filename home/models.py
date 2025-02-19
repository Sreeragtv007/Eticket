from django.db import models

# Create your models here.


class Events(models.Model):
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    discription = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=50)
    event_img = models.ImageField(upload_to='event_image')
    price = models.IntegerField()
    
    
    class Meta:
        ordering = ['date']
    
    def __str__(self):
        return self.name