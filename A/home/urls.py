from django.urls import path, include
from . import views

app_name = 'home'

bucket_urlpatterns = [
    path('', views.BucketHome.as_view(), name='bucket'),
    path('delete_obj/<str:key>/', views.DeleteBucketObject.as_view(), name='delete_obj_bucket'),

]

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('bucket/', include(bucket_urlpatterns)),
    path('<slug:slug>/', views.ProductDetileView.as_view(), name='product_detile'),
]
