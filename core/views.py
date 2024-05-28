from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .models import Category, Item
from .forms import SignupForm
from django.contrib import messages

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    category = Category.objects.all()
    return render(request,'core/index.html',{
        'categories': category,
        'items':items,
    })

def contact(request):
    return render(request,'core/contact.html')

def signup(request):

    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():

            form.save()
            return redirect('/login/')
       
    else:
        form=SignupForm()


    return render(request, 'core/signup.html',{
        'form': form,
    })

def logout_view(request):
    logout(request)
    return render(request, 'core/logout.html', {'redirect_time': 5})