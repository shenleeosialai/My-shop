from django.urls import path
from . import views
# from .views import card_view

app_name = 'shop'
urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list,
         name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('api/countdown/', views.countdown_data, name='countdown_data'),
]
