from django.urls import path, include
from computer import views

app_name = 'computer'

urlpatterns = [
    path('', views.computers, name='computers'),
    path('<int:computer_id>/', views.computer_details, name="computer_details")
]