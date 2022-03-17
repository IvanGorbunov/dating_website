from django.urls import path, include


urlpatterns = [
    path('clients/', include('clients.urls')),
]