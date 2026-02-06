from django.urls import path
from .views import(
    ListResourceView,
    CreateResourceView,
    DetailResourceView,
    UpdateResourceView,
    DeleteResourceView
)

urlpatterns = [
    path('', ListResourceView, name="resource-page"),
    path('<int:id>/', DetailResourceView, name="resource-detail"),
    path('create/', CreateResourceView, name="resource-create"),
    path('<int:id>/update/', UpdateResourceView, name="resource-update"),
    path('<int:id>/delete/', DeleteResourceView, name="resource-delete"),
]