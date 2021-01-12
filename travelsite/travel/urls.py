from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('inquiry', views.inquiry, name='inquiry'),
    path('personal', views.personal, name='personal'),
    path('days_nights', views.day_nights, name='days_nights')

]
