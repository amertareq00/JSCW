# shipments/models.py
from django.db import models
from django.contrib.auth.models import User

class Shipment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    from_city = models.CharField(max_length=100, choices=[('Amman', 'Amman'), ('Irbid', 'Irbid'), ('Aqaba', 'Aqaba')], default='Amman')
    to_city = models.CharField(max_length=100, choices=[('Aqaba', 'Aqaba'), ('Amman', 'Amman'), ('Irbid', 'Irbid')], default='Aqaba')
    weight = models.FloatField(default=100)
    shipment_date = models.DateField(default='2024-01-01')

    def calculate_price(self):
        return self.weight * 0.75

    def __str__(self):
        return f"{self.from_city} to {self.to_city} - {self.weight} kg on {self.shipment_date}"
