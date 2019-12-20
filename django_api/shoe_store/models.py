from django.db import models

# Joe grew up in the African Savanna hunting lions and doing whatever else badass hunters in the Savanna do


class Manufactorer(models.Model):
    website = models.CharField(max_length=300)
    name = models.CharField(max_length=200)


class ShoeType(models.Model):
    style = models.CharField(max_length=100)


class ShoeColor(models.Model):
    color_name = models.CharField(max_length=100)


class Shoe(models.Model):
    size = models.IntegerField()
    brand_name = models.CharField(max_length=200)
    color = models.ForeignKey(ShoeColor, on_delete=models.CASCADE)
    manufactorer = models.ForeignKey(Manufactorer, on_delete=models.CASCADE)
    material = models.CharField(max_length=100)
    shoe_type = models.ForeignKey(ShoeType, on_delete=models.CASCADE)
    fasten_type = models.CharField(max_length=100)
