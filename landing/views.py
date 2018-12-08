from django.shortcuts import render
from .forms import SubscriberForm
from products.models import *
import datetime


def landing(request):
    name = 'Siusarna'
    current_day = '14.08.2018'
    form =SubscriberForm(request.POST or None)

    if request.method =="POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)

        new_form = form.save()

    return render(request, 'landing/landing.html', locals())

def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_new = products_images.filter(product__type__id=3).order_by("-product")[:4]
    products_images_hot = products_images.filter(product__type__id=4)
    products_images_sightseening = products_images.filter(product__type__id=5)
    products_images_popular = products_images.filter(product__type__id=6)
    products_images_all = products_images
    return render(request, 'landing/home.html', locals())
# Create your views here.
