# Generated by Django 4.1.6 on 2023-02-09 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_product_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'permissions': [('set_published_status', 'Can publish Product'), ('add_Product', 'Can add Product')]},
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.BooleanField(choices=[(True, 'available'), (False, 'no item')], default=True, max_length=20),
        ),
    ]
