from django.urls import path

from catalog import views

urlpatterns = {
    path('', views.home),
    path('contact/', views.contact),
}
