# Generated by Django 5.1.3 on 2024-11-22 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='brand',
            name='founded_at',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='brand',
            name='headquarters',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='brand',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='brands/logos/'),
        ),
    ]
