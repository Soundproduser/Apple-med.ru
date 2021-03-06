# Generated by Django 3.2.6 on 2021-09-03 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VitaminAndMineral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('brand', models.CharField(max_length=255, verbose_name='Бренд')),
                ('country', models.CharField(max_length=255, verbose_name='Страна')),
                ('dosage', models.CharField(max_length=255, verbose_name='Дозировка')),
                ('package', models.CharField(max_length=255, verbose_name='Упаковка')),
                ('release_form', models.CharField(max_length=255, verbose_name='Форма выпуска')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category', verbose_name='Категория')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('brand', models.CharField(max_length=255, verbose_name='Бренд')),
                ('country', models.CharField(max_length=255, verbose_name='Страна')),
                ('dosage', models.CharField(max_length=255, verbose_name='Дозировка')),
                ('package', models.CharField(max_length=255, verbose_name='Упаковка')),
                ('release_form', models.CharField(max_length=255, verbose_name='Форма выпуска')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category', verbose_name='Категория')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
