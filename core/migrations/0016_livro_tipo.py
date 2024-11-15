# Generated by Django 5.1 on 2024-08-27 17:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0015_tipo"),
    ]

    operations = [
        migrations.AddField(
            model_name="livro",
            name="tipo",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="livros",
                to="core.tipo",
            ),
        ),
    ]
