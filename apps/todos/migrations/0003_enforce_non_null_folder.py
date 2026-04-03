from django.db import migrations, models
import django.db.models.deletion


def fill_null_todo_folders(apps, schema_editor):
    Folder = apps.get_model("folders", "Folder")
    Todo = apps.get_model("todos", "Todo")

    fallback_folder, _ = Folder.objects.get_or_create(
        name="Uncategorized",
        defaults={"color": "#6366F1", "icon": "folder", "position": 0},
    )
    Todo.objects.filter(folder__isnull=True).update(folder=fallback_folder)


class Migration(migrations.Migration):

    dependencies = [
        ("folders", "0005_alter_folder_unique_together_alter_folder_color_and_more"),
        ("todos", "0002_alter_todo_options_remove_todo_completed_at_and_more"),
    ]

    operations = [
        migrations.RunPython(fill_null_todo_folders, migrations.RunPython.noop),
        migrations.AlterField(
            model_name="todo",
            name="folder",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="todos", to="folders.folder"),
        ),
    ]
