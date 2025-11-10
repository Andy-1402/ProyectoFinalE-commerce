from django.urls import path
from .views import HomeView, CategoriaListView, ProductoDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('categoria/<str:categoria>/', CategoriaListView.as_view(), name='categoria_list'),
    path('producto/<int:pk>/', ProductoDetailView.as_view(), name='producto_detail'),
]
