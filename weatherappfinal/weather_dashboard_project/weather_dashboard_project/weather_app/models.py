from django.db import models

class SearchHistory(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.FloatField()
    humidity = models.IntegerField()
    condition = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.city} - {self.temperature}°C"
