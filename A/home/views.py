from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
# Create your views here.
from django.views import View
from .models import Product
from .import tasks



class HomeView(View):
    def get(self, request):
        products = Product.objects.filter(available=True)
        return render(request, 'home/home.html', {'products': products})


class ProductDetileView(View):
    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        return render(request, 'home/detile.html', {'product': product})

    def post(self, request):
        pass


class BucketHome(View):
    template_name = 'home/bucket.html'

    def get(self, requeat):
        objects = tasks.all_objects_tasks
        return render(requeat, self.template_name, {'objects': objects})


class DeleteBucketObject(View):
    def get(self, request, key):
        tasks.delete_obj_bucket_task.delay(key)
        messages.success(request, 'your object will be delete soon', 'info')
        return redirect('home:bucket')