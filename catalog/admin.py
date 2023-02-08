from django.contrib import admin

# from catalog.models import Student

# admin.site.register(Student)
# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ('id', 'first_name', 'last_name')
#     search_fields = ('first_name', 'last_name')
#     list_filter = ('last_name',)

from .models import Category, Product, Record, Subject

# @admin.register(Person)
# class PersonAdmin(admin.ModelAdmin):
#     search_fields = ("last_name__startswith",)
admin.site.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category', 'category_description']
    list_filter = ['category']

    # prepopulated_fields = {'slug': ('name',)}

class ProductAdmin(admin.ModelAdmin):
    # '','preview', , 'date_of_creation', 'date_last_change'
    list_display = ['id', 'product_name', 'category', 'price_per_unit']
    list_filter = ['category']
    search_fields = ("product_name", "product_description", )
    # list_editable = ['']
    # prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)
class RecordAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'image', 'id_public']
    prepopulated_fields = {"slug": ("title",)}
admin.site.register(Record, RecordAdmin)

admin.site.register(Subject)
