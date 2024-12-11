from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm
from django.http import HttpResponse
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContactForm
from .models import ContactMessage
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
import random
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .forms import CheckoutForm
from django.shortcuts import render
from .models import Category, Product
import stripe
import json
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string


otp_storage = {}




def index(request):
    return render(request,'index.html')

def privacy(request):
    return render(request,'privacy.html')



def about(request):
    return render(request,'about.html')



def cart(request):
    return render(request,'cart.html')
def success(request):
    return render(request,'success.html')

def cancel(request):
    return render(request,'cancel.html')

def contact(request):
    return render(request,'contact.html')


from django.contrib import messages


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save to database
            contact_message = ContactMessage.objects.create(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            
            # Send email with HTML content
            subject = f"New Contact Message from {contact_message.username}"
            from_email = 'kbmagoda2024@gmail.com'  # Replace with your email
            recipient_list = ['kbmagoda2024@gmail.com']  # Replace with the recipient's email(s)

            # HTML content for email with purple background
            html_content = f"""
            <html>
            </head>
            <body>
           <div style="font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #FF0000;">
                <!-- Optional animated GIF (on top of the red background) -->
             <div style="background-color: rgba(255, 255, 255, 0.8); padding: 20px; border-radius: 8px; max-width: 600px; margin: auto;">
                        <h1 style="color: #007BFF; font-size: 2rem;">New Contact Message</h1>
                        <p style="color: #555555; font-size: 1.1rem;"><strong>Name:</strong> {contact_message.username}</p>
                        <p style="color: #555555; font-size: 1.1rem;"><strong>Email:</strong> {contact_message.email}</p>
                        <p><strong>Message:</strong></p>
                        <p style="color: #555555; font-size: 1.1rem;"><strong>Email:</strong> {contact_message.message}</p>
                        <div style="text-align: center; margin-top: 20px; font-size: 0.9rem; color: #888888;">
                            <p>&copy; 2024 Your Website Name. All rights reserved.</p>
                        </div>
                    </div>
                    </div>
                    </div>
            """

            try:
                # Use EmailMultiAlternatives for HTML emails
                email = EmailMultiAlternatives(subject, '', from_email, recipient_list)
                email.attach_alternative(html_content, "text/html")
                email.send()
                
                # Add success message
                messages.success(request, "Thank you for your message! An email notification has been sent.")
                return redirect('index')  # Replace 'index' with the name of your index URL
            except Exception as e:
                messages.error(request, f"Message saved, but email failed to send. Error: {e}")
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def subscribe(request):
    if request.method == "POST":
        email = request.POST.get("email")
        
        # HTML content for the email
        html_message = """
        <html>
        <body>
            <div style="font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #FF0000;">
                <!-- Optional animated GIF (on top of the red background) -->
                <div style="background: url('https://your-animated-gif-url.com/your-animation.gif') no-repeat center center fixed; background-size: cover; padding: 50px 0;">
                    <div style="background-color: rgba(255, 255, 255, 0.8); padding: 20px; border-radius: 8px; max-width: 600px; margin: auto;">
                        <h1 style="color: #007BFF; font-size: 2rem;">Thank You for Subscribing!</h1>
                        <p style="color: #555555; font-size: 1.1rem;">We're excited to have you on board. You'll start receiving updates, news, and exclusive offers from us soon.</p>
                        <p style="color: #555555; font-size: 1.1rem;">Stay tuned for our latest content and promotions!</p>
                        <div style="text-align: center; margin-top: 20px; font-size: 0.9rem; color: #888888;">
                            <p>&copy; 2024 Your Website Name. All rights reserved.</p>
                        </div>
                    </div>
                </div>
            </div>
        </body>
        </html>
        """
        
        # Send the email with HTML content
        send_mail(
            subject="Subscription Confirmation",
            message="This is a confirmation email. Please view it in an HTML-compatible email client.",
            from_email="your_email@gmail.com",
            recipient_list=[email],
            html_message=html_message,  # This is the HTML body
        )
        
        # Display success message on the same page
        messages.success(request, "Subscription email sent!")

    return render(request, "subscribe.html")

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('auth_login')
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():  # CaptchaField will be validated as part of form.is_valid()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('product_list')  # Replace with your desired redirect URL
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid form submission.')

    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

@login_required
def welcome(request):
    return render(request, 'welcome.html')

def logout_view(request):
    logout(request)
    return redirect('auth_login')


def forgot_password(request):
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            users = User.objects.filter(email=email)
            for user in users:
                token = default_token_generator.make_token(user)
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                reset_link = request.build_absolute_uri(f"/reset/{uid}/{token}/")
                subject = "Password Reset Request"
                message = render_to_string('password_reset_email.html', {'reset_link': reset_link})
                send_mail(subject, message, 'noreply@yourdomain.com', [email])
            messages.success(request, "Password reset email sent.")
            return redirect("login")
    else:
        form = PasswordResetForm()
    return render(request, "forgot_password.html", {"form": form})


def verify_otp(request, username):
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        if int(entered_otp) == otp_storage.get(username):
            user = User.objects.get(username=username)
            user.is_active = True
            user.save()
            messages.success(request, "Account verified successfully!")
            return redirect('login')
        else:
            messages.error(request, "Invalid OTP. Please try again.")
    return render(request, 'verify_otp.html', {'username': username})



def checkout_view(request):
    if request.method == "POST":
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # Process the form data
            data = form.cleaned_data
            print("Billing Info:", data)  # Replace with actual processing logic
            return render(request, 'success.html', {"data": data})
    else:
        form = CheckoutForm()
    
    return render(request, 'checkout.html', {"form": form})




stripe.api_key = settings.STRIPE_SECRET_KEY

def product_list(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'product_list.html', {'categories': categories, 'products': products})

def product_by_category(request, category_id):
    category = Category.objects.get(id=category_id)
    products = category.products.all()
    return render(request, 'product_list.html', {'categories': Category.objects.all(), 'products': products, 'current_category': category})

# views.py

@csrf_exempt
def create_checkout_session(request):
    if request.method == "POST":
        data = json.loads(request.body)
        cart = data['cart']
        total = data['total']
        username = data['user']

        try:
            # Create a Stripe Checkout session
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[
                    {
                        'price_data': {
                            'currency': 'zar',
                            'product_data': {
                                'name': item['name'],
                            },
                            'unit_amount': int(item['price'] * 100),  # Convert to cents
                        },
                        'quantity': item['quantity'],
                    }
                    for item in cart
                ],
                mode='payment',
                 success_url=request.build_absolute_uri('/success/'),
                cancel_url=request.build_absolute_uri('/cancel/')   # URL on cancellation
            )
            return JsonResponse({'session_url': checkout_session.url})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=400)


