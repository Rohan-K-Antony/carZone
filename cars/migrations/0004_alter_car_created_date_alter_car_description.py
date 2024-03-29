# Generated by Django 4.1.5 on 2023-01-15 13:29

import ckeditor.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cars", "0003_alter_car_created_date_alter_car_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="created_date",
            field=models.DateTimeField(
                blank=True, default=datetime.datetime(2023, 1, 15, 18, 59, 44, 450530)
            ),
        ),
        migrations.AlterField(
            model_name="car", name="description", field=ckeditor.fields.RichTextField(),
        ),
    ]
