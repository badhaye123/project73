# Generated by Django 3.2.6 on 2021-09-14 04:32

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
                ('Date', models.DateField()),
                ('Provider', models.CharField(max_length=30)),
                ('Name_of_product', models.CharField(max_length=30)),
                ('Price', models.IntegerField()),
                ('Quality', models.IntegerField()),
                ('Amount', models.IntegerField()),
                ('Stock', models.IntegerField()),
            ],
        ),
    ]
