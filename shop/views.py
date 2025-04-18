from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddProductForm
from .models import Category, Product
from .recommender import Recommender
from .models import Countdown
from django.http import JsonResponse


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category, available=True)
        return render(request, 'shop/product/list.html', {
            'category': category,
            'categories': categories,
            'products': products,
        })

    # Get all featured categories from the database
    featured_sections = []
    featured_categories = Category.objects.filter(featured=True)

    for c in featured_categories:
        featured_products = Product.objects.filter(category=c, available=True)[:6]
        featured_sections.append({
            'category': c,
            'products': featured_products
        })

    return render(request, 'shop/product/list.html', {
        'category': None,
        'categories': categories,
        'featured_sections': featured_sections,
    })


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    r = Recommender()
    recommended_products = r.suggest_products_for([product], 4)
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form,
                   'recommended_products': recommended_products})


def countdown_data(request):
    countdown = Countdown.objects.last()
    return JsonResponse({
        'title': countdown.title,
        'end_date': countdown.end_date.isoformat()
    })
