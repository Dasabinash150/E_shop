from django.shortcuts import render
from django.http import HttpResponse


# from django.template import Template , Context
from app.models import Category,Product


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
