# Generated by Django 3.2.3 on 2021-05-17 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('country_code', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('country_name', models.CharField(max_length=255)),
                ('continent', models.CharField(max_length=124)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('city_code', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('city_name', models.CharField(max_length=255)),
                ('country_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='city_country', to='avia.country')),
            ],
        ),
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airport_code', models.CharField(max_length=5, unique=True)),
                ('airport_name', models.CharField(max_length=255)),
                ('type_code', models.CharField(max_length=2)),
                ('city_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='airport_city', to='avia.city')),
                ('country_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='airport_country', to='avia.country')),
            ],
        ),
    ]