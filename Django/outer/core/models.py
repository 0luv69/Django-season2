from django.db import models

# Create your models here.
class normal(models.Model):
    name = models.CharField(max_length=100)
    des = models.TextField()



    def __str__(self):
        return f"{self.name} ----- {self.dec}"

