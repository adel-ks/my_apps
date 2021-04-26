from django.urls import path
from .views import *


urlpatterns = [
	path('', product_list, name='product_list'),
	path('<int:product_id>/', product_details, name='product_details'),
]