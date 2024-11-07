from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from .models import Customer, Tent, Decor, Catering, Miscellaneous,Seatings,Organiser, Available_Equipment, BookedEquipment
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.http import JsonResponse
from django.contrib import messages
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
import json

def index(request):
    return render(request, 'index.html')

def organiser(request):
    if request.method == 'POST':
        name = request.POST['business-name']
        location = request.POST['location']
        email = request.POST['email']
        phone = request.POST["phone"]
        services = request.POST.getlist('services')
        services_str = ', '.join(services)
        info = request.POST['additional-info']

        organiser = Organiser(
            bus_name=name,
            bus_loc=location,
            bus_email=email,
            bus_phone=phone,
            bus_services=services_str,
            add_info=info
        )
        organiser.save()
        messages.success(request, "Successfully captured your details. We'll communicate soon!")
        return redirect('organiser')

    return render(request, 'organiser.html')

def terms(request):
    return render(request, 'terms.html')

def about(request):
    return render(request, 'about.html')

def question(request):
    return render(request, 'question.html')

def password_reset(request):
    if request.method == 'POST':
        email = request.POST['email']
        try:
            user = Customer.objects.get(email=email)
            # Generate a password reset token (you may want to implement this part)
            # For simplicity, this example sends a plain email
            send_mail(
                'Password Reset Request',
                'Please click the link below to reset your password:\n\nhttp://127.0.0.1:8000/password_reset/',
                'noreply@rentalBox.com',
                [user.email],
                fail_silently=False,
            )
            messages.success(request, "A password reset link has been sent to your email address.")
        except Customer.DoesNotExist:
            messages.error(request, "No account found with that email address.")
    
    return render(request, 'password_reset.html')

def view_all(request):
    tents = Tent.objects.all()
    decor = Decor.objects.all()
    catering = Catering.objects.all()
    tables_and_chairs = Seatings.objects.all()
    miscellaneous = Miscellaneous.objects.all()

    context = {
        'tents': tents,
        'decor': decor,
        'catering': catering,
        'tables_and_chairs': tables_and_chairs,
        'miscellaneous': miscellaneous
    }
    
    return render(request, 'view_all.html', context)

def equipment(request, item):
    if item == 'Tent':
        items = Tent.objects.all()
        name = 'Tents'

    elif item == 'Decor':
        items = Decor.objects.all()
        name = 'Decors'

    elif item == 'Catering':
        items = Catering.objects.all()
        name = 'Caterings'

    elif item == 'Seatings':
        items = Seatings.objects.all()
        name = 'Seatings'

    else:
        items = Miscellaneous.objects.all()
        name = 'Miscellaneous'

    return render(request, 'equipment.html', {'items':items, 'name':name})


def profile(request, name):
        tents = Tent.objects.all()
        decor = Decor.objects.all()
        catering = Catering.objects.all()
        tables_and_chairs = Seatings.objects.all()
        miscellaneous = Miscellaneous.objects.all()
        curr_user = get_object_or_404(Customer, username= name)

        context = {
        'tents': tents,
        'decor': decor,
        'catering': catering,
        'tables_and_chairs': tables_and_chairs,
        'miscellaneous': miscellaneous,
        'user' : curr_user
    }
        return render(request, 'profile.html', context)

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

       
        if Customer.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken.")
            return redirect('signup')
        
        if Customer.objects.filter(email=email).exists():
            messages.error(request, "Email is already in use.")
            return redirect('signup')

        
        customer = Customer(username=username, email=email)
        customer.set_password(password)  
        customer.save()
        messages.success(request, "Account created successfully. Please log in.")
        return redirect('login')

    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        try:
            customer = Customer.objects.get(email=email)
            if customer.check_password(password):
                # Manually set session to authenticate customer
                request.session['customer_id'] = customer.id
                return redirect(reverse('profile', kwargs={'name': customer.username}))
            else:
                messages.error(request, "Incorrect password.")
                return redirect('login')
        except Customer.DoesNotExist:
            messages.error(request, "User with this username does not exist.")
            return redirect('login')

    return render(request, 'login.html')


def customer_home(request):
    return render(request, 'customer_base.html')

def logout(request):
    if 'customer_id' in request.session:
        del request.session['customer_id']
    return redirect('login')

@login_required
def update_customer(request, name):
    customer = get_object_or_404(Customer, username=name)  
    if request.method == 'POST':
       
        new_name = request.POST.get('name')
        new_email = request.POST.get('email')
        new_phone = request.POST.get('phone')
        new_address = request.POST.get('address')
        new_profile_pic = request.FILES.get('image')

        
        if new_name:
            customer.username = new_name
        if new_email:
            customer.email = new_email
        if new_phone:
            customer.mobile = new_phone
        if new_address:
            customer.address = new_address
        if new_profile_pic:
            customer.profile_pic = new_profile_pic

        
        customer.save()
        messages.success(request, "Profile updated successfully!")
        return redirect(reverse('profile', kwargs={'name': customer.username}))

    return redirect(reverse('profile', kwargs={'name': customer.username}))

def add_to_cart(request, item_id, item_type):
    
    cart = request.session.get('cart', {})

    
    if item_type == "tent":
        item = Tent.objects.get(id=item_id)
    elif item_type == "decor":
        item = Decor.objects.get(id=item_id)
    elif item_type == "catering":
        item = Catering.objects.get(id=item_id)
    elif item_type == "seatings":
        item = Seatings.objects.get(id=item_id)
    elif item_type == "miscellaneous":
        item = Miscellaneous.objects.get(id=item_id)
    else:
        return JsonResponse({"error": "Invalid item type"}, status=400)

    item_key = f"{item_type}_{item_id}"
    if item_key in cart:
        cart[item_key]['quantity'] += 1  
    else:
        cart[item_key] = {
            'name': item.name,
            'price_per_day': item.price_per_day,
            'quantity': 1
        }

    request.session['cart'] = cart
    request.session.modified = True
    return JsonResponse({"message": "Item added to cart", "cart_count": len(cart)})

def get_cart(request):
    cart = request.session.get('cart', {})
    total_price = sum(item['price_per_day'] * item['quantity'] for item in cart.values())
    total_quantity = sum(item['quantity'] for item in cart.values())
    return JsonResponse({"cart": cart, "total_price": total_price, "total_quantity": total_quantity})


@csrf_exempt
def check_availability(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        start_date = datetime.strptime(data['start_date'], '%Y-%m-%d').date()
        end_date = datetime.strptime(data['end_date'], '%Y-%m-%d').date()

        # Retrieve all bookings overlapping with the selected date range
        booked_equipment = BookedEquipment.objects.filter(
            start_date__lte=end_date, end_date__gte=start_date
        )

        # Calculate available quantities for each item in the available equipment
        available_equipment = Available_Equipment.objects.all()
        response_data = []

        for equipment in available_equipment:
            total_booked_quantity = sum(
                item.quantity for item in booked_equipment.filter(equipment_id=equipment.id)
            )
            available_quantity = equipment.quantity - total_booked_quantity

            if available_quantity > 0:
                response_data.append({
                    'name': equipment.name,
                    'quantity': available_quantity
                })

        return JsonResponse({'available_equipment': response_data})

    return JsonResponse({'error': 'Invalid request'}, status=400)

def test(request):
    return render(request, 'test.html')

def payment(request):
    return render(request, 'payment.html')