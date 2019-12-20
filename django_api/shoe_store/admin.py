from django.contrib import admin
from . models import ShoeType, ShoeColor, Shoe, Manufactorer

# Register your models here.
admin.site.register(ShoeColor)
admin.site.register(ShoeType)
admin.site.register(Shoe)
admin.site.register(Manufactorer)