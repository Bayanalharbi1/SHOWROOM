# Generated by Django 5.1.3 on 2024-11-23 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0006_alter_car_price_alter_car_specs_alter_color_hex_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='car_type',
            field=models.CharField(choices=[('Sedan', 'Sedan'), ('SUV', 'SUV'), ('Coupe', 'Coupe'), ('Hatchback', 'Hatchback'), ('Convertible', 'Convertible'), ('Truck', 'Truck'), ('Van', 'Van'), ('Other', 'Other')], default='Other', max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='colors',
            field=models.ManyToManyField(to='cars.color'),
        ),
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='car',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='car',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='car_photos/'),
        ),
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='car',
            name='specs',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.PositiveIntegerField(),
        ),
    ]
