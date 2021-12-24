from django.urls import path, include

app_name = 'ApiApp'

urlpatterns = [
    path('/users', include('UserProfileApp.urls', namespace='UserProfileApp')),
    path('/product', include('ProductApp.urls', namespace='ProductApp')),
    path('/system', include('ModuleApp.urls', namespace='ModuleApp')),
    path('/status', include('StatusApp.urls', namespace='StatusApp')),
]
