from django.shortcuts import render
from .serializers import ItemSerializer
from .models import Item
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from stripetest import settings
import stripe



class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer



@api_view(['POST'])
def buy(request, pk):
    item = Item.objects.get(id=pk)
    stripe.api_key = settings.STRIPE_API_KEY
    pay=stripe.PaymentIntent.create(
        amount=item.price*100,
        currency="eur",
    )

# Create your views here.
