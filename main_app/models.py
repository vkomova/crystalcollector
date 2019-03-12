from django.db import models

class Crystal(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField()
    healingproperties = models.TextField()

    def __str__(self):
        return self.name

