# Generated by Django 4.2.2 on 2023-08-29 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("book", "0005_change_issuebook_model"),
    ]

    operations = [
        migrations.AlterField(
            model_name="issuebook",
            name="book",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="book.book"
            ),
        ),
    ]
