from django.shortcuts import render,redirect
from django.http import HttpResponse


# from django.template import Template , Context
from app.models import Category,Product
from django.contrib.auth import authenticate,login
from app.models import UserCreateForm


def Master(request):
    return render(request, "master.html")


def homePage(request):
    category = Category.objects.all()

    categoryID = request.GET.get('category')

    if categoryID:
        product = Product.objects.filter(sub_category = categoryID).order_by('-id')
    else:
        product = Product.objects.all()

    context = {
        'category': category,
        'product': product,
    }
    return render(request, "index.html", context )

def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password1'],
            )
            login(request, new_user)
            return redirect('index')
    else:
        form = UserCreateForm()

        
    context = {
            'form':form,
        }
    return render(request,'registration/signup.html',context)

def contact(request):
    
    return render(request, 'contact.html')