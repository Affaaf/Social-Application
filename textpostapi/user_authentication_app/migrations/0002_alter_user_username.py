# Generated by Django 4.2.2 on 2023-06-17 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user_authentication_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(max_length=255, null=True),
        ),
    ]