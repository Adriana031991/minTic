"""tienda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.urls import path
from appTienda import views
#from appTienda.views.productoListView import ProductoListView
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('user/', views.UserCreateView.as_view()), #post
    path('user/<int:pk>/', views.UserDetailView.as_view()), #put
    path('user/detailview/', views.UserDetailView.as_view()), #consulta usuario desde token get sin parametro
    path('producto/crear/', views.ProductoCreateView.as_view()), # post productos
    path('producto/<int:pk>/', views.ProductoDetailView.as_view()), #para get , put y delete individual
    path('producto/',  views.ProductoView.as_view()), #lista de productos
    path('factura/', views.CreateFacturaView.as_view()), # post
    path('factura/<int:pk>/',  views.FacturaDetailView.as_view()), # get
    path("facturas/", views.FacturaListView.as_view()), #listar facturas

]

