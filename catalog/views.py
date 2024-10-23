from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.forms import inlineformset_factory
from catalog.forms import VersionForm
from catalog.models import Product, Version, Category

from catalog.forms import ProductForm
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
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(**kwargs)
        if self.request.user == self.object.owner:
            ProductFormset = inlineformset_factory(Product, Version, VersionForm, extra=1)
            if self.request.method == 'POST':
                context_data['formset'] = ProductFormset(self.request.POST, instance=self.object)
            else:
                context_data['formset'] = ProductFormset(instance=self.object)
        return context_data

    def get_success_url(self):
        return reverse("catalog:product_details", args=[self.kwargs.get('pk')])

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')