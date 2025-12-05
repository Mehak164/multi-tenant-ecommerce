from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import Order
from .serializers import OrderSerializer

class OrderListCreateView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(tenant=self.request.user.tenant)

    def perform_create(self, serializer):
        serializer.save(
            tenant=self.request.user.tenant,
            customer=self.request.user
        )

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(tenant=self.request.user.tenant)
