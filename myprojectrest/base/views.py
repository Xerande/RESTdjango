from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from rest_framework import viewsets
from .serializers import ItemSerializer
# Create your views here.


def home(request):
    return HttpResponse('Hello, its me')


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer