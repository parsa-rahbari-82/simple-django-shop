from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddForm


def home(request, slug=None):
    products = Product.objects.all()
    categories = Category.objects.filter(is_sub=False)
    if slug:
        category = get_object_or_404(Category, slug=slug)
        products = products.filter(category=category)
    return render(request, 'store/home.html', {'products': products, 'categories': categories})


def product_detail(request, main_cat, slug):
    product = get_object_or_404(Product, slug=slug)
    pcat = get_object_or_404(Category, slug=main_cat)
    psub_cats = [i for i in product.category.filter(is_sub=True)]
    similar_products = Product.objects.filter(category__name=pcat).filter(~Q(id=product.id)).order_by('?')[:5]
    form = CartAddForm()
    return render(request, 'store/product_detail.html', {'product': product, 'similar_products': similar_products,
                                                         'form': form, 'pcat': pcat, 'psub_cats': psub_cats})
