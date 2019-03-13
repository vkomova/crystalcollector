from django.db import models
from django.urls import reverse
from datetime import date

USETYPE = (
    ('M', 'Mental'),
    ('P', 'Physical'),
    ('S', 'Spiritual')
)

class Country(models.Model):
  name = models.CharField('Country Name', max_length=50)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('countries_detail', kwargs={'pk': self.id})

class Crystal(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField()
    healingproperties = models.TextField('Healing Properties')
    countries = models.ManyToManyField(Country)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'crystal_id': self.id})
    
    def used_for_today(self):
        return self.uses_set.filter(date=date.today()).count() >= len(USETYPE)

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

class Photo(models.Model):
    url = models.CharField(max_length=200)
    crystal = models.ForeignKey(Crystal, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for crystal_id: {self.crystal_id} @"