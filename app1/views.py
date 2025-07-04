from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm
from .models import Order
from datetime import datetime  # Add this at the top with your other imports

# This view becomes your homepage that decides where to go
def home_view(request):
    if request.session.get('user_authenticated', False):
        return redirect('dashboard')
    else:
        return redirect('login')

def login_view(request):
    if request.session.get('user_authenticated', False):
        return redirect('dashboard')
        
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            if username == 'admin' and password == 'admin123':
                request.session['user_authenticated'] = True
                request.session['username'] = username
                request.session['user_first_name'] = 'John'
                messages.success(request, 'Login successful!')
                return redirect('dashboard')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    
    return render(request, 'app1/login.html', {'form': form})

def dashboard(request):
    if not request.session.get('user_authenticated', False):
        messages.error(request, 'Please login to access the dashboard.')
        return redirect('login')

    context = {
        'user_first_name': request.session.get('user_first_name', 'User'),
        'username': request.session.get('username', 'admin'),
    }

    return render(request, 'app1/dashboard.html', context)

def logout_view(request):
    request.session.flush()
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')

# The second index() is removed or renamed to something else (like home_view)
def index_view(request):
    return render(request, 'index.html')

def neworder(request):
  return render(request, 'neworder.html')




def neworder(request):
    return render(request, 'neworder.html')



def save_order(request):
    if request.method == 'POST':
        customer = request.POST.get('customer')
        place = request.POST.get('place')
        phone = request.POST.get('phone')
        quantity = request.POST.get('quantity')

        if not quantity:
            messages.error(request, "Quantity is required.")
            return redirect('order')

        try:
            quantity = int(quantity)
        except ValueError:
            messages.error(request, "Quantity must be a number.")
            return redirect('order')

        Order.objects.create(
            customer=customer,
            place=place,
            phone=phone,
            quantity=quantity
        )

        messages.success(request, "Order placed successfully.")
        return redirect('order')

    return redirect('order')


def order_view(request):
    return render(request, 'order.html')


from django.utils import timezone

def save_order(request):
    if request.method == 'POST':
        customer = request.POST.get('customer')
        place = request.POST.get('place')
        phone = request.POST.get('phone')
        quantity = request.POST.get('quantity')

        if not quantity:
            messages.error(request, "Quantity is required.")
            return redirect('order')

        try:
            quantity = int(quantity)
        except ValueError:
            messages.error(request, "Quantity must be a number.")
            return redirect('order')

        # Create the order
        order = Order.objects.create(
            customer=customer,
            place=place,
            phone=phone,
            quantity=quantity
        )

        # Store order info in session
        request.session['order_customer'] = customer
        request.session['order_id'] = order.id  # Use the auto-generated ID
        request.session['order_date'] = timezone.now().strftime('%Y-%m-%d %H:%M:%S')

        messages.success(request, "Order placed successfully.")
        return redirect('order')

    return redirect('order')


def order_view(request):
    # Get the authenticated user's first name if available
    user_first_name = request.session.get('user_first_name', None)
    
    context = {
        'customer': request.session.get('order_customer', user_first_name or 'Guest'),
        'order_id': request.session.get('order_id', '0000'),
        'order_date': request.session.get('order_date', timezone.now().strftime('%Y-%m-%d %H:%M:%S')),
    }
    return render(request, 'order.html', context)