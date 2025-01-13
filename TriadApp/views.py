
from django.shortcuts import render, redirect
from django.contrib import messages
import pyrebase
from .firebase import auth, database

def index(request):
    return render(request, 'TriadApp/index.html')
        
def superadmin(request):
    return render(request, 'TriadApp/superadmin/super_admin.html')


def admin(request):
    return render(request, 'TriadApp/admin/admin.html')


def inventory(request):
    return render(request, 'TriadApp/admin/admin-inventory.html')

def login(request):
    return render(request, 'TriadApp/login.html')



def add_product(request):
    if request.method == 'POST':
        # Get product data from the form
        product_name = request.POST.get('product_name')
        category = request.POST.get('category')
        price = request.POST.get('price')
        stock = request.POST.get('stock')

        # Prepare the data to add to Firebase
        product_data = {
            'name': product_name,
            'category': category,
            'price': price,
            'stock': stock
        }

        # Push single product data to Firebase
        new_entry_ref = database.child('Data').child(product_name).set(product_data)


        return render(request, 'TriadApp/admin/admin-inventory.html', {'message': 'Product added successfully!'})

    return render(request, 'TriadApp/admin/admin-inventory.html')
