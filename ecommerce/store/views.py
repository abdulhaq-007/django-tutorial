from django.shortcuts import render

# Create your views here.
def home(request):
    context = {}
    return render(request, 'index.html', context)

def shop(request):
    context = {}
    return render(request, 'shop.html', context)

def cart(request):
    context = {}
    return render(request, 'cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'checkout.html', context)