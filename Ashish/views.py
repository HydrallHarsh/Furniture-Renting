from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import logout
from Ashish.form import FurnitureForm
from templetes import *
from django.shortcuts import render
from Ashish.models import Furniture

# Create your views here.


def add_to_cart(request, pk):
    furniture = get_object_or_404(Furniture, pk=pk)
    furniture.is_in_cart = True  # Assuming you set a flag or manage a cart elsewhere
    furniture.save()
    return redirect('shop')  # Redirect back to the shop page or wherever you need


def home(request):
    furniture_list = Furniture.objects.all()
    print(furniture_list)
    return render(request, 'home.html', {'furniture_list': furniture_list})


def signup(request):
    return render(request, 'signup.html')


def logout_view(request):
    logout(request)
    return redirect('home')


def profile(request):
    return render(request, 'profile.html')


def settings(request):
    return render(request, 'settings.html')


def about_us(request):
    return render(request, 'about_us.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print(username, password)
            return redirect(home)
        else:
            messages.info(request, "Invalid username or password")
            return redirect(login)
    return render(request, 'login.html')


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        print(username, email, password)
        if User.objects.filter(username=username).exists():
            messages.info(
                request, "Username already exists. Try with different username.")
            return redirect(signup)
        else:
            user = User.objects.create_user(
                username=username, email=email, password=password)
            user.set_password(password)
            user.save()
            return redirect(login)
    else:
        return render(request, 'signup.html')


def shop(request):
    furniture_list = Furniture.objects.all()
    return render(request, 'shop.html', {'furniture_list': furniture_list})


def furniture_detail(request, pk):
    furniture_detail = get_object_or_404(Furniture, pk=pk)
    return render(request, 'shop.html', {'furniture_detail': furniture_detail})


def furniture_create(request):
    if request.method == 'POST':
        form = FurnitureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('shop')
    else:
        form = FurnitureForm()
    return render(request, 'shop.html', {'form': form})


def furniture_edit(request, pk):
    furniture_edit = get_object_or_404(Furniture, pk=pk)
    if request.method == 'POST':
        form = FurnitureForm(request.POST, request.FILES,
                             instance=furniture_edit)
        if form.is_valid():
            form.save()
            return redirect('shop')
    else:
        form = FurnitureForm(instance=furniture_edit)
    return render(request, 'shop.html', {'edit_form': form})


def furniture_delete(request, pk):
    furniture_delete = get_object_or_404(Furniture, pk=pk)
    if request.method == 'POST':
        furniture_delete.delete()
        return redirect('shop')
    return render(request, 'shop.html', {'furniture_delete_confirm': furniture_delete})
