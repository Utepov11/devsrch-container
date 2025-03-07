# Generated by Django 5.1.2 on 2024-11-19 16:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("inventory", "0006_computer_computer_id_printer_printer_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="ReportLog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("report_name", models.CharField(max_length=255)),
                ("generated_at", models.DateTimeField(auto_now_add=True)),
                ("file_path", models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name="computer",
            name="id",
        ),
        migrations.RemoveField(
            model_name="printer",
            name="id",
        ),
        migrations.AlterField(
            model_name="computer",
            name="computer_id",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="printer",
            name="printer_id",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
