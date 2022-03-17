from django.urls import path

from clients import views

app_name = 'clients'

urlpatterns = [
    path('create/', views.UserViewSet.as_view({'post': 'create'}), name='create_client'),
]
