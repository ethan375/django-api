from rest_framework import viewsets
from . models import Manufactorer, Shoe, ShoeColor, ShoeType
from . serializers import ManufactorerSerializer, ShoeTypeSerializer, ShoeColorSerializer, ShoeSerializer


class ManufactorerViewSet(viewsets.ModelViewSet):
    queryset = Manufactorer.objects.all()
    serializer_class = ManufactorerSerializer


class ShoeTypeViewSet(viewsets.ModelViewSet):
    queryset = ShoeType.objects.all()
    serializer_class = ShoeTypeSerializer


class ShoeColorViewSet(viewsets.ModelViewSet):
    queryset = ShoeColor.objects.all()
    serializer_class = ShoeColorSerializer


class ShoeViewSet(viewsets.ModelViewSet):
    queryset = Shoe.objects.all()
    serializer_class = ShoeSerializer 