from django.shortcuts import render
from rest_framework import viewsets


from rest_framework import viewsets, permissions

from vision.models import Orders
from vision.serializers import OrdersSerializer


# Create your views here.
class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = OrdersSerializer



def index(request):
    orders = Orders.objects.all()
    return render(request, "vision/index.html", {"orders": orders})