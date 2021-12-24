from django.urls import path, include

from .views import SubSystemViewSet

app_name = 'ModuleApp'

urlpatterns = [
    path('', SubSystemViewSet.as_view({'get': 'list'})),
    path('/add', SubSystemViewSet.as_view({'post': 'create'})),
    path('<int:pk>', SubSystemViewSet.as_view({'get': 'retrieve'})),

]
