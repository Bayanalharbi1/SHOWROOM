# Generated by Django 5.1.3 on 2024-11-23 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0003_alter_brand_about_alter_brand_founded_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='headquarters',
            field=models.CharField(default='other', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='brand',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='brand_logos/'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]