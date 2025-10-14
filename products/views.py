from rest_framework import viewsets
from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class updateProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer    
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class updateOrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer    
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

