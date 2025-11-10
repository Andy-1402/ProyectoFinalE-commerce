from django.views.generic import ListView, DetailView, TemplateView
from .models import Producto

class HomeView(TemplateView):
    template_name = "productos/home.html"


class CategoriaListView(ListView):
    model = Producto
    template_name = "productos/categoria_list.html"
    context_object_name = "productos"

    def get_queryset(self):
        categoria_nombre = self.kwargs.get('categoria')
        return Producto.objects.filter(categoria__nombre__iexact=categoria_nombre, disponible=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categoria'] = self.kwargs.get('categoria').capitalize()
        return context


class ProductoDetailView(DetailView):
    model = Producto
    template_name = "productos/producto_detail.html"
    context_object_name = "producto"
