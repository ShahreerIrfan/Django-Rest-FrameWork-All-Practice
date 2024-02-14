from django.db import models

# Create your models here.
class carList(models.Model):
    name = models.CharField(max_length = 40)
    description = models.CharField(max_length = 500)
    active = models.BooleanField(default = False)
    chassisNumber = models.CharField(max_length=20,blank=True,null=True)
    price = models.DecimalField(max_digits=9,decimal_places=2,blank=True,null=True)
    def __str__(self) -> str:
        return self.name
    
class ShowRoom(models.Model):
    name = models.CharField(max_length=300)
    location = models.CharField(max_length = 100)
    website = models.URLField(max_length = 100)

    def __str__(self) -> str:
        return self.name