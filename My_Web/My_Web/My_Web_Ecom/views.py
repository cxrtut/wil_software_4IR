from django.shortcuts import render
from  django.http import HttpResponse

def index(request):
    return render(request,'homepage.html')

def livestock(request):
   # livestock_products = Livestock.objects.all()  # Query all livestock products from the database
    return render(request, 'livestock.html')

def vegetables(request):
  #  vegetable_products = Vegetable.objects.all()  # Query all vegetable products from the database
    return render(request, 'vegetables.html')

def product_detail(request, product_id):
  #  product = Product.objects.get(id=product_id)  # Query a specific product by its ID
    return render(request, 'product_detail.html')
