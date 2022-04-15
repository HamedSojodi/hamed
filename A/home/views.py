from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views import View
from .models import Product
from .tasks import all_objects_tasks


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
        objects = all_objects_tasks
        return render(requeat, self.template_name, {'objects': objects})
