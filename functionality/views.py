from django.shortcuts import render
from .serializers import ItemSerializer
from .models import Item
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from stripetest import settings
from django.shortcuts import redirect
import stripe
from rest_framework.response import Response



class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer



@api_view(['GET'])
def buy(request, pk):
    item = Item.objects.get(id=pk)
    stripe.api_key = settings.STRIPE_API_KEY
    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item.name,
                },
                'unit_amount': item.price,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://google.com',
        cancel_url='http://facebook.com',
    )
    return Response(session.url)
    # return redirect(session.url, code=303)

# Create your views here.
