# Generated by Django 4.1.5 on 2023-01-20 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contacts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="created_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
