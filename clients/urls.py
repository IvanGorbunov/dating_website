from django.urls import path

from clients import views

app_name = 'clients'

urlpatterns = [
    path('create/', views.UserViewSet.as_view({'post': 'create'}), name='create_client'),
    path('<int:pk>/match/', views.UserMatchViewSet.as_view({'post': 'like'}), name='like'),
    path('list/', views.UserViewSet.as_view({'get': 'list'}), name='list'),
]
