from django import forms

from catalog.models import Product, Subject, Category


class SubjectForm(forms.ModelForm):
    class Meta:
        # t = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        model = Subject
        fields = '__all__'  # ('product_name', 'product_description', 'preview', 'price_per_unit', 'category')
        def __str__(self):
            return f"""{self.product_name}{self.preview}  {self.product_description} {self.price_per_unit} {self.status}   """


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
