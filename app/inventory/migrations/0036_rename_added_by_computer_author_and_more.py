# Generated by Django 5.1.2 on 2024-12-02 16:28

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("inventory", "0035_delete_user"),
    ]

    operations = [
        migrations.RenameField(
            model_name="computer",
            old_name="added_by",
            new_name="author",
        ),
        migrations.RenameField(
            model_name="printer",
            old_name="added_by",
            new_name="author",
        ),
    ]
