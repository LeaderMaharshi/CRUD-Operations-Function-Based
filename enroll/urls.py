from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_show, name="addandshow"),
    path('remove/<int:id>/', views.delete_data, name="delete_data"),
    path('<int:id>/', views.update_data, name="update_data"),
]