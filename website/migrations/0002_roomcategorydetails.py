# Generated by Django 2.0.2 on 2020-08-24 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Roomcategorydetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomoption', models.CharField(max_length=200)),
                ('roomprice', models.IntegerField()),
                ('roomcategoryid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Roomcategory')),
            ],
        ),
    ]
