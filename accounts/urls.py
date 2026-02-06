from django.urls import path
from . import views

urlpatterns = [
    # ... other patterns
    path('logout/', views.logoutView, name='logout'),
]