from .models import Brand, Mobile


def list_all_brands():
    query = Brand.objects.all()
    return query


def list_all_mobiles():
    query = Mobile.objects.all()
    return query


def price_of_mobile_with_model(model):
    query = Mobile.objects.get(price__in=model)
    return query


def most_expensive_mobile():
    query = Mobile.objects.order_by('-price').first()

    return query


def all_mobiles_with_brand_of(brand_name):
    query = Mobile.objects.filter(name=brand_name)
    return query


def all_available_mobiles_with_price_in_range(min_price, max_price):
    query = ...
    return query
