# this code has come from the quickstart guide at https://www.django-rest-framework.org/tutorial/quickstart

from . models import Shoe, ShoeType, Manufactorer, ShoeColor
from rest_framework import serializers


class ManufactorerSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Manufactorer
        fields = ['website', 'name']


class ShoeTypeSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = ShoeType
        fields = ['style']


class ShoeColorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ShoeColor
        fields = ['color_name']

class ShoeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Shoe
        fields = ['size', 'brand_name', 'color', 'manufactorer', 'material', 'shoe_type', 'fasten_type']