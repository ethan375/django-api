from rest_framework import viewsets
from . models import Manufactorer, Shoe, ShoeColor, ShoeType
from . serializers import ManufactorerSerializer, ShoeTypeSerializer, ShoeColorSerializer, ShoeSerializer


class ManufactorerViewSet(viewsets.ModelViewSet):
    queryset = Manufactorer.objects.all()
    serializer_class = ManufactorerSerializer