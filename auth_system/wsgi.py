"""
WSGI config for auth_system project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'auth_system.settings')

application = get_wsgi_application()

import json
from django.http import JsonResponse

def create_checkout_session(request):
    if request.method == 'POST':
        try:
            # Parse JSON from request body
            body = json.loads(request.body.decode('utf-8'))
            
            # Access cart data from the parsed JSON
            cart = body.get('cart', [])
            line_items = []

            # Build line items for Stripe
            for item in cart:
                line_items.append({
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': item['name'],
                        },
                        'unit_amount': int(float(item['price']) * 100),  # Amount in cents
                    },
                    'quantity': item['quantity'],
                })

            # Create Stripe checkout session
            import stripe
            stripe.api_key = "sk_test_..."  # Replace with your secret key
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                mode='payment',
                line_items=line_items,
                success_url='https://your-site.com/success',
                cancel_url='https://your-site.com/cancel',
            )
            return JsonResponse({'id': session.id})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)
