# Generated by Django 4.2.2 on 2023-08-29 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("reader", "0001_create_models"),
        ("book", "0007_change_issuebook_model"),
    ]

    operations = [
        migrations.AlterField(
            model_name="onhandbook",
            name="reader",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="reader.reader"
            ),
        ),
    ]