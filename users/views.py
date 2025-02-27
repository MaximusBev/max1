from .models import CustomUser, Product
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomRegisterForm, CustomLoginForm, ProductForm
from django.contrib import messages
from django.urls import reverse

def register(request):
    if request.method == "POST":
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password1"])  # Хешування пароля
            user.save()
            login(request, user)
            return redirect("home")  # Перенаправлення після успішної реєстрації
    else:
        form = CustomRegisterForm()
    return render(request, "users/register.html", {"form": form})

def user_login(request):
    if request.method == "POST":
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = CustomLoginForm()
    return render(request, "users/login.html", {"form": form})

def custom_logout(request):
    logout(request)
    return redirect('/')

def products(request):
    return render(request, 'products.html')  # Створи шаблон products.html

def contact(request):
    return render(request, 'contact.html')  # Створи шаблон contact.html

@login_required
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

@login_required
def orders_view(request):
    return render(request, 'orders.html')

@login_required
def users_list(request):
    users = CustomUser.objects.all()  # Використовуємо CustomUser
    return render(request, 'users/users_list.html', {'users': users})

@login_required
def delete_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if user.is_superuser:
        messages.error(request, "Не можна видалити адміністратора!")
    else:
        user.delete()
        messages.success(request, "Користувач успішно видалений.")
    return redirect(reverse('users_list'))

@login_required
def make_admin(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    user.is_staff = True
    user.is_superuser = True
    user.save()
    messages.success(request, "Користувача зроблено адміністратором.")
    return redirect('users_list')

@login_required
def edit_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    
    if request.method == "POST":
        user.username = request.POST['username']
        user.email = request.POST['email']
        user.save()
        messages.success(request, "Користувач успішно оновлений.")
        return redirect(reverse('users_list'))

    return render(request, 'users/edit_user.html', {'user': user})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products/product_detail.html', {'product': product})


def products(request):
    all_products = Product.objects.all()  # Отримуємо всі продукти
    return render(request, 'products/products.html', {'products': all_products})

def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products')  # Перенаправлення на список продуктів
    else:
        form = ProductForm()
    return render(request, 'products/add_product.html', {'form': form})
