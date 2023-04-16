from rest_framework import viewsets
from .serializers import CatSerializer
from .models import Category


# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('title')
    serializer_class = CatSerializer


