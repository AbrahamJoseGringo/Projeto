# Generated by Django 5.1 on 2024-08-27 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0014_rename_autor_livro_autores"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tipo",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("descricao", models.CharField(max_length=100)),
            ],
        ),
    ]
