from django import forms

from catalog.models import Product, Subject, Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            for name, field in self.fields.items():
                field.widgets.attrs['class'] = 'form-control'

class SubjectForm(forms.ModelForm):
    class Meta:
        # t = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        model = Subject
        fields = '__all__'  # ('product_name', 'product_description', 'preview', 'price_per_unit', 'category')
        # def __str__(self):
        #     return f"""{self.product_name}{self.preview}  {self.product_description} {self.price_per_unit} {self.status}   """


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
