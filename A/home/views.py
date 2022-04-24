from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
# Create your views here.
from django.views import View

from utils import IsAdminUsermixin
from .models import Product, Category
from . import tasks


class HomeView(View):
    def get(self, request, category_slug=None):
        products = Product.objects.filter(available=True)
        categories = Category.objects.filter(is_sub=False)
        print(categories)
        print(products)
        print(category_slug)
        if category_slug:
            print(category_slug)
            category = Category.objects.get(slug= category_slug)
            products=products.filter(category=category )
        else:
            print('not fond')
        return render(request, 'home/home.html', {'products': products, 'categories': categories})


class ProductDetileView(View):
    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        return render(request, 'home/detile.html', {'product': product})

    def post(self, request):
        pass


class BucketHome(IsAdminUsermixin, View):
    template_name = 'home/bucket.html'

    def get(self, request):
        objects = tasks.all_objects_tasks
        return render(request,  self.template_name, {'objects': objects})


class DeleteBucketObject(IsAdminUsermixin, View):
    def get(self, request, key):
        tasks.delete_obj_bucket_task.delay(key)
        messages.success(request, 'your object will be delete soon', 'info')
        return redirect('home:bucket')


class DownloadBucketObject(IsAdminUsermixin, View):
    def get(self, request, key):
        tasks.download_obj_bucket_task(key)
        messages.success(request, 'your object will be download soon', 'info')
        return redirect('home:bucket')
