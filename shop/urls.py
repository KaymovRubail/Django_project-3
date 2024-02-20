"""
URL configuration for shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from product.views import hello_view,goodbye_view,current_date_view,main_view,products_view1,product__detail_view,category_view,products_view2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/',hello_view),
    path('goodbye/',goodbye_view),
    path('current_date/',current_date_view),
    path('',main_view),
    path('cate/',category_view),
    path('cate/products/<int:id>/',products_view1),
    path('cate/products/<int:id>/products/<int:prid>/',product__detail_view),
    path('products/products/<int:prid>/',product__detail_view),
    path('products/',products_view2)

]