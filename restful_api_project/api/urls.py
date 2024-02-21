from django.urls import path
from . import views


urlpatterns = [

    path('', views.hello_world),
    path('items/', views.items, name='items'),
    path('create-item/', views.create_item, name='create_items'),

    ]
