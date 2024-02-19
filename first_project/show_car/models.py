from django.db import models
from django.core.validators import MaxLengthValidator,MinLengthValidator

# Create your models here.

    
class ShowRoom(models.Model):
    name = models.CharField(max_length=300)
    location = models.CharField(max_length = 100)
    website = models.URLField(max_length = 100)

    def __str__(self) -> str:
        return self.name
    
class carList(models.Model):
    name = models.CharField(max_length = 40)
    description = models.CharField(max_length = 500)
    active = models.BooleanField(default = False)
    chassisNumber = models.CharField(max_length=20,blank=True,null=True)
    price = models.DecimalField(max_digits=9,decimal_places=2,blank=True,
    null=True)
    showroom = models.ForeignKey(ShowRoom, on_delete=models.CASCADE, related_name="cars",)
    def __str__(self) -> str:
        return self.name
    
class Review(models.Model):
    ratings = models.IntegerField(validators = [MaxLengthValidator,MinLengthValidator])
    comments = models.CharField(max_length = 300,null = True)
    car = models.ForeignKey(carList,on_delete = models.CASCADE,related_name = "Review",null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "The rating of " + self.car.name+":--" + str(self.ratings)
    
class CarSpecification(models.Model):
    CAR_CATEGORIES = [
        ('sedan', 'Sedan'),
        ('hatchback', 'Hatchback'),
        ('SUV', 'SUV'),
        ('truck', 'Truck'),
        ('electric', 'Electric')
    ]

    CarName = models.CharField(max_length=50)
    CarPrice = models.IntegerField()
    Category = models.CharField(max_length=50, choices=CAR_CATEGORIES)
    Description = models.TextField()

    def __str__(self):
        return self.CarName
    

# ...

    
