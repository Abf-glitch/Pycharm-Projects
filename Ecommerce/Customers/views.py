from lib2to3.fixes.fix_input import context

from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django_daraja.mpesa.core import MpesaClient

from Customers.forms import CustomerForm, CustomerRegistrationForm
from Customers.models import Customer
from Customers.serializers import CustomerSerializer



# Create your views here.
def index(request):
    data = Customer.objects.all()
    context = {'data': data}
    return render(request,'Index.html',context)

def about(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('about')
    else:
            form = CustomerRegistrationForm()
    return render(request,'about.html', {'form':form})


def gallery(request):
    return render(request,'Gallery.html')
def login(request):
    return render(request,'Login.html')
def signup(request):
    return render(request,'Signup.html')

def edit(request,id):
    customer = get_object_or_404(Customer,id=id)
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            messages.error(request, 'Error!!Please check the details')
    else:
        form = CustomerRegistrationForm(instance=customer)
    return render(request, 'edit.html', {'form':form,'customer':customer})
def delete(request,id):
    customer = get_object_or_404(Customer,id=id)
    try:
        customer.delete()
        messages.success(request, 'Customer has been deleted successfully')
    except Exception as e:
        messages.error(request, 'Error!!Customer not deleted')
    return redirect('index')


def customerapi(request):
    customer = Customer.objects.all()
    serializer = CustomerSerializer(customer, many=True)
    return JsonResponse(serializer.data, safe=False)

def darajaapi(request,):
    cl = MpesaClient()
    phone_number = '0740523454'
    amount = 1
    account_reference = 'Ecommerce'
    transaction_desc = 'Description'
    callback_url = 'https://darajambili.herokuapp.com/express-payments/';
    response = cl.stk_push(phone_number, amount, account_reference,transaction_desc, callback_url)
    return  HttpResponse(response)
