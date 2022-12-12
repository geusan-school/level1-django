# Generated by Django 4.1.3 on 2022-12-05 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.PositiveIntegerField(default=0, verbose_name='product stock count')),
                ('category', models.CharField(max_length=20, verbose_name='product category')),
                ('price', models.PositiveIntegerField(verbose_name='product price')),
                ('name', models.CharField(max_length=255, verbose_name='product name')),
                ('description', models.CharField(max_length=2000, verbose_name='product description')),
                ('sell', models.PositiveIntegerField(default=0, verbose_name='sell count')),
            ],
            options={
                'unique_together': {('category', 'name')},
            },
        ),
    ]