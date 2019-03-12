from django.db import models
from django.urls import reverse
from datetime import date

USETYPE = (
    ('M', 'Mental'),
    ('P', 'Physical'),
    ('S', 'Spiritual')
)

class Crystal(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField()
    healingproperties = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'crystal_id': self.id})

class Uses(models.Model):
    date = models.DateField('Date Used', default=date.today)
    used = models.CharField(
        max_length=1,
        choices=USETYPE,
        default=USETYPE[0][0],
    )
    crystal = models.ForeignKey(Crystal, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_used_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']