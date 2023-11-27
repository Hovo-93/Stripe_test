from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .serializers import ItemSerializer
from .models import Item
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from stripetest import settings
from django.shortcuts import redirect
import stripe
from rest_framework.response import Response





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
    return JsonResponse({'session_id': session.id})


# Create your views here.
def item_detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    # Replace item details and descriptions accordingly
    context = {
        'item_name': item.name,
        'item_description': item.description,
        'item_price': item.price,
        'publishable_key': 'pk_test_51OGlf1EQj5G4dxj6XtLjrPcmqXmGfQbcMlg4hGPIAcO4qG2A59lFNZeVyJRpsx86fJRtwD0tU1FSlvxnWVgPscDg00ijnJ4uaJ',
        'item_id': item_id,
    }
    return render(request, 'temp.html', context)