from django.db import models

class Temp_Data(models.Model):
    name = models.CharField(max_length=100)
    temperature = models.FloatField()
#    latest = models.FloatField()
#    times = models.IntegerField()

    def __str__(self):
        return self.name

class Pulse_Data(models.Model):
    name = models.CharField(max_length=100)
    hRate = models.FloatField()
#    initial = models.FloatField()
#    times = models.IntegerField()

    def __str__(self):
        return self.name