from django.urls import path, include

from .views import SubSystemViewSet, ModuleViewSet

app_name = 'ModuleApp'

urlpatterns = [
    path('', SubSystemViewSet.as_view({'get': 'list'})),
    path('/add', SubSystemViewSet.as_view({'post': 'create'})),
    path('<int:pk>', SubSystemViewSet.as_view({'put': 'update', 'delete': 'destroy', 'get': 'retrieve'})),

    path('<int:systemID>/add', ModuleViewSet.as_view({'post': 'create'})),
    path('<int:systemID>/module<int:pk>', ModuleViewSet.as_view({'put': 'update', 'delete': 'destroy', 'get': 'retrieve'})),

]
