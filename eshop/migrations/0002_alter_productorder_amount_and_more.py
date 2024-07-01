# Generated by Django 5.0.6 on 2024-06-30 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productorder',
            name='amount',
            field=models.IntegerField(db_column='amount', default=1),
        ),
        migrations.RenameField(
            model_name='productorder',
            old_name='amount',
            new_name='_amount',
        ),
    ]
