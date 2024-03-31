# Generated by Django 5.0.3 on 2024-03-29 04:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='ecommerce/pimg')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('category', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app.category')),
                ('sub_category', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app.sub_category')),
            ],
        ),
    ]
