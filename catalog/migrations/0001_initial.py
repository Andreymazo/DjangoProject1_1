# Generated by Django 4.1.6 on 2023-02-04 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=250, verbose_name='Category')),
                ('category_description', models.CharField(max_length=250, verbose_name='Category description')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=250, verbose_name='Naimenovanie Producta')),
                ('product_description', models.CharField(blank=True, max_length=250, null=True, verbose_name='Product description')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='records')),
                ('price_per_unit', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('date_of_creation', models.DateField(auto_now_add=True)),
                ('date_last_change', models.DateField(auto_now=True)),
                ('status', models.CharField(choices=[('active', 'available'), ('inactive', 'no item')], default='active', max_length=20)),
                ('category', models.ForeignKey(blank=True, max_length=100, on_delete=django.db.models.deletion.CASCADE, related_name='Category', to='catalog.category', verbose_name='Category description')),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('slug', models.CharField(max_length=50, verbose_name='Slug')),
                ('content', models.TextField(max_length=50, verbose_name='Content')),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to='records')),
                ('date_of_creation', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('id_public', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('views_controller', models.IntegerField(blank=True, default=0, null=True, verbose_name='Счетчик просмотров')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_content', models.CharField(max_length=150)),
                ('product_name_again', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product')),
            ],
        ),
    ]
