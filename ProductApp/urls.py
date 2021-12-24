from django.urls import path, include

from .views import ProductViewSet

app_name = 'ProductApp'

urlpatterns = [
    path('', ProductViewSet.as_view({'get': 'list'}), name='product'),
    path('<int:pk>', ProductViewSet.as_view({'get': 'retrieve'}), name='product'),
]