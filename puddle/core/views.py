from django.shortcuts import render

from items.models import Category, Item


def index(request):
        items = Item.objects.filter(is_sold=False)[0:6]
        categories=Category.objects.all()
        return render(request, 'core/index.html', {
                'Categories':categories,
                'items':items
        })

def contact(request):
        return render(request, 'core/contact.html')