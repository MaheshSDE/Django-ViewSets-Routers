#from rest_framework.generics import ListCreateAPIView
#from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer


# Create your views here.
# class ProductListView(ListCreateAPIView):
#     queryset         = Product.objects.all()
#     serializer_class = ProductSerializer

# class ProductDetailView(RetrieveUpdateDestroyAPIView):
#     queryset         = Product.objects.all()
#     serializer_class = ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset         = Product.objects.all()
    serializer_class = ProductSerializer