from django.urls import path
from django.conf.urls.static import static
from catalog.apps import CatalogConfig
from catalog.formset_views import ProductUpdateWithSubject
from config import settings
from catalog.views import products, contact_us, RecordListView, RecordCreateView, RecordUpdateView, RecordDeleteView, \
    RecordDetailView, ProductListView, ProductUpdateView, \
    ProductCreateView, ProductDeleteView, ProductDetailView, \
    change_status, CategoryListView  # , RecordCreateView, crab1,ProductCreateView,

# , contacts, hello,
app_name = CatalogConfig.name

urlpatterns = [
    # path('', hello, name='home'),#WRONG
    path('', products, name='home'),
    path('contact_us/', contact_us, name='contacts'),
    path('category/', CategoryListView.as_view(), name='Category_List'),
    path('products/', ProductListView.as_view(), name='Product_list'),
    path('create_products/<int:pk>/', ProductCreateView.as_view(), name='Product_create'),
    path('create_products/', ProductCreateView.as_view(), name='Product_create'),
    # path('create_products/<int:pk>/subjects/', ProductUpdateWithSubject.as_view(), name='update_withsubject'),


    path('delete_products/<int:pk>/', ProductDeleteView.as_view(), name='Product_delete'),
    path('detail_products/<int:pk>/', ProductDetailView.as_view(), name='Product_detail'),

    # path('update_products/<int:pk>/', ProductUpdateView.as_view(), name='Product_form'),
    path('update_products/<int:pk>/', ProductUpdateView.as_view(), name='Product_form'),
    # path('contact_us/crab1/', crab1, name='crab1'),#Созданы 2 одинаковые ветки
    # для тренировки, через класс RecordListView и черерз функцию render in file view
    path('Rec_list/', RecordListView.as_view(), name='Rec_list'),
    path('create/', RecordCreateView.as_view(), name='create'),

    # path('create/', RecordCreateView.as_view(), name='create'),
    path('update/<int:pk>/', RecordUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', RecordDeleteView.as_view(), name='delete'),
    path('detail/<int:pk>/', RecordDetailView.as_view(), name='detail'),
    path('status/<int:pk>/', change_status, name='status'),
]