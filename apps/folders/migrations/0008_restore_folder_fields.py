from django.db import migrations, models
from django.utils import timezone


class Migration(migrations.Migration):

    dependencies = [
        ("folders", "0007_remove_folder_created_at_remove_folder_position_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="folder",
            options={"ordering": ["position", "created_at"]},
        ),
        migrations.AddField(
            model_name="folder",
            name="color",
            field=models.CharField(default="#6366F1", max_length=7),
        ),
        migrations.AddField(
            model_name="folder",
            name="icon",
            field=models.CharField(default="folder", max_length=50),
        ),
        migrations.AddField(
            model_name="folder",
            name="position",
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name="folder",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, default=timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="folder",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, default=timezone.now),
            preserve_default=False,
        ),
    ]
