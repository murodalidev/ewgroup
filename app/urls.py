from django.urls import path
from .views import index, about, why, service, contact

app_name = 'app'

urlpatterns = [
    path('', index, name='index'),
    path('why-choose/', why, name='why'),
    path('about/', about, name='about'),
    path('services/', service, name='service'),
    path('contact/', contact, name='contact'),
]
