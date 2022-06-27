from tkinter import E
from unicodedata import category
from django.shortcuts import render, get_object_or_404
from category.models import Category
from store.models import Product

def store(request):
    categories = Category.objects.all()
    products = Product.objects.all().filter(is_available=True)
    context = {'categories': categories, 'products': products}
    return render(request, 'store/store.html', context)

def product_by_category(request, category_slug):
    categories = Category.objects.all()
    categories_slug = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.all().filter(category=categories_slug, is_available=True)
    context = {'categories_slug': categories_slug, 'products': products, 'categories': categories}
    return render(request, 'store/store_by_cat.html', context)

def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e

    context = {'single_product': single_product}
    return render(request, 'store/product_detail.html', context)
