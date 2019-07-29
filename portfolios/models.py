from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Portfolio(models.Model):
    name = models.CharField(max_length=255)
    client = models.CharField(max_length=255)
    pub_date = models.DateField()
    price = models.FloatField()
    rate = models.PositiveIntegerField(default=8, validators=[MinValueValidator(1), MaxValueValidator(10)])
    description = models.TextField()
    feedback = models.TextField()
    live_link = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

    def images(self):
        return self.image.all()



class PortfolioImage(models.Model):
    image = models.ImageField(upload_to="media/portfolio/images/")
    portfolio = models.ForeignKey(Portfolio, related_name="image", on_delete=models.CASCADE)

    def __str__(self):
        return self.portfolio.name
