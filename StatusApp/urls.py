from django.urls import path, include

from .views import StatusViewSet, ProblemViewSet, PriorityViewSet

app_name = 'StatusApp'

urlpatterns = [
    path('/status', StatusViewSet.as_view({'get': 'list'}), name='StatusType'),
    path('/problem', ProblemViewSet.as_view({'get': 'list'}), name='ProblemType'),
    path('/priority', PriorityViewSet.as_view({'get': 'list'}), name='PriorityType'),
]