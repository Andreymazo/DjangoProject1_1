from django import forms
from django.db import transaction
from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from catalog.forms import SubjectForm, ProductForm
from catalog.models import Product, Subject


class ProductCreateWithSubject(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:Product_list')
    template_name = 'catalog/product_withsubject.html'

    # def clean_product_content(self):
    #     t = ['казинo', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
    #     if self.request.method == 'POST':
    #         # form = ProductForm(request.POST, request.FILES)
    #         for i in t:
    #             if self.product_content == i:
    #                 raise ValueError('Nedopustimie slova')
    # def get_success_url(self):
    #     return reverse('catalog:Product_list', args=[self.object.pk])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        FormSet = inlineformset_factory(self.model, Subject, form=SubjectForm, extra=1)

        if self.request.method == 'POST':
            formset = FormSet(self.request.POST, instance=self.object)
        else:
            formset = FormSet(instance=self.object)

        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        print(self.request.method)
        with transaction.atomic():
            self.object = form.save()
            if formset.is_valid():
                formset.instance = self.object
                formset.save()
            else:
                return super(ProductCreateWithSubject, self).form_invalid(form)
        return super(ProductCreateWithSubject, self).form_valid(form)


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'
