from django.shortcuts import render

# Create your views here.
def index():
    return render(request, 'customer/index.html')