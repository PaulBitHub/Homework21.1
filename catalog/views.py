from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from catalog.models import Product


class ProductListView(ListView):
    model = Product

class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product_details.html"

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object

class ProductCreateView(CreateView):
    model = Product
    fields = ("product_name", "product_description", "price", "category", "image")
    success_url = reverse_lazy('catalog:product_list')

class ProductUpdateView(UpdateView):
    model = Product
    fields = ("product_name", "product_description", "price", "category", "image")
    success_url = reverse_lazy('catalog:product_list')

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')