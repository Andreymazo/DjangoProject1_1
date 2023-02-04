from django import forms

from catalog.models import Product, Subject, Category


class SubjectForm(forms.ModelForm):
    class Meta:
        # t = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        model = Subject
        fields = '__all__'  # ('product_name', 'product_description', 'preview', 'price_per_unit', 'category')


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
