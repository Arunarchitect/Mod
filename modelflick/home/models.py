from django.db import models

# Create your models here.
class services(models.Model):
    Name = models.CharField(max_length=100)
    area_of_site = models.DecimalField(max_digits=10, decimal_places=2)
    type_choices = [
        ('residential', 'Residential'),
        ('hospital', 'Hospital'),
        ('educational', 'Educational'),
        ('commercial', 'Commercial'),
        ('assembly', 'Assembly'),
        ('storage', 'Storage')
    ]
    Your_dream_building = models.CharField(max_length=20, choices=type_choices)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.Name}{self.area_of_site}{self.Your_dream_building}{self.created}"
    