# Generated by Django 5.1.3 on 2024-11-23 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0002_brand_about_brand_founded_at_brand_headquarters_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='about',
            field=models.TextField(default='No description provided'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='brand',
            name='founded_at',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='brand',
            name='headquarters',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]