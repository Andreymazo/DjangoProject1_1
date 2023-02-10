import regex as regex
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import CASCADE

import catalog
from users.models import User

# from django.contrib.auth.models import Permission
# permissions = Permission.objects.all()

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    category = models.CharField(max_length=250, verbose_name="Category")
    category_description = models.CharField(max_length=250, verbose_name="Category description")

    def __str__(self):
        return f'{self.category}'


class Product(models.Model):
    STATUS_ACTIV = True
    STATUS_INACTIV = False
    STATUSES = (
        (STATUS_ACTIV, 'available'),
        (STATUS_INACTIV, 'no item')
    )

    product_name = models.CharField(max_length=250, verbose_name='Naimenovanie Producta')

    product_description = models.CharField(max_length=250, verbose_name="Product description", **NULLABLE)
    preview = models.ImageField(upload_to='records', **NULLABLE)
    category = models.ForeignKey(Category, related_name="Category", blank=True, max_length=100,
                                 verbose_name="Category description",
                                 on_delete=models.CASCADE)
    price_per_unit = models.DecimalField(max_digits=6, decimal_places=2, **NULLABLE)
    date_of_creation = models.DateField(auto_now_add=True)
    date_last_change = models.DateField(auto_now=True)
    published_status = models.BooleanField(choices=STATUSES, default=STATUS_ACTIV, max_length=20)

    # for perm in Product_permission:
    #     User.user_permissions.add(perm)
    class Meta:
        permissions = [
            ("set_published_status", "Can publish Product"),
            ("add_Product", "Can add Product"),
        ]


    # class Meta:
    #     permissions = (("group 1", "Can view 3 suggestions"), ("group 2", "Can view 6 suggestions"),)
        # for perm in permissions:
        #     User.user_permissions.add(perm)
        # for perm in permissions:
            # User.user_permissions.add(perm)#has_perm(catalog.set_published_status_product))
        # print(User.user_permissions)
        # from django.contrib.auth.models import Permission
        # permissions = Permission.objects.filter(user=User)
        # for perm in permissions:
        #     User.user_permissions.add(perm)

        # @permission_required("blog.view_post") ###############FBV
        # def post_list_view(request):
        #     """ Работа с доступами в FBV """
        #     return HttpResponse()
        ###################################################3
    def save(self, *args, **kwargs):
        t = ['казинo', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        if self.product_name in t:
            raise ValidationError('Nedopustimie slova')
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return f"""{self.product_name}{self.preview}  {self.product_description} {self.price_per_unit} {self.status}   """  # {self.id}


class Subject(models.Model):
    product_name_again = models.ForeignKey(Product, on_delete=CASCADE)  # , related_name="product_name"
    # product_name_again = models.CharField(max_length=50, verbose_name='prod name')
    product_content = models.CharField(max_length=150)#validators=[regex(r'\%казино%')],

    def __str__(self):
        return f"{self.product_name_again} {self.product_content} "



    def clean(self):

        # t = ['казинo', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        # for i in t:
        #     print(i)
        if self.product_content == 'казино':# and self.pub_date is not None
            raise ValidationError('Entry may not be казино')
        return self.product_content


    # def save(self, *args, **kwargs):
    #     t = ['казинo', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
    #     if self.product_name_again in t:
    #         raise ValidationError('Nedopustimie slova')
    #     return super().save(*args, **kwargs)


class Record(models.Model):
    title = models.CharField(max_length=50, verbose_name="Заголовок")
    slug = models.CharField(max_length=50, verbose_name="Slug")
    content = models.TextField(max_length=50, null=False, verbose_name='Content')
    image = models.ImageField(upload_to="records", **NULLABLE, default=None)

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания", **NULLABLE)
    id_public = models.BooleanField(default=True, verbose_name="Опубликовано")
    views_controller = models.IntegerField(default=0, verbose_name="Счетчик просмотров", **NULLABLE)

    def __str__(self):
        return f'{self.title} {self.content} {self.image} {self.id_public}'
