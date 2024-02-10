from django.db import models

# Create your models here.
class carList(models.Model):
    name = models.CharField(max_length = 40)
    description = models.CharField(max_length = 500)
    active = models.BooleanField(default = False)
    def __str__(self) -> str:
        return self.name