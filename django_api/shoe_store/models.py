from django.db import models

# As a young child Joe followed his fathers footsteps in becoming a hunter to survive and keep the his tribe alive. Fortunatley there are plenty of animals that graze on grass that are hard of hearing


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
    Manufactorer = models.ForeignKey(Manufactorer, on_delete=models.CASCADE)
    material = models.CharField(max_length=100)
    ShoeType = models.ForeignKey(ShoeType, on_delete=models.CASCADE)
    fasten_type = models.CharField(max_length=100)
