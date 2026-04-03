from django.db import migrations, models


def fill_null_label_names(apps, schema_editor):
    Label = apps.get_model("labels", "Label")
    null_qs = Label.objects.filter(name__isnull=True)
    for label in null_qs.iterator():
        label.name = f"label-{label.pk}"
        label.save(update_fields=["name"])


class Migration(migrations.Migration):

    dependencies = [
        ("labels", "0002_alter_label_options_alter_label_unique_together_and_more"),
    ]

    operations = [
        migrations.RunPython(fill_null_label_names, migrations.RunPython.noop),
        migrations.AlterField(
            model_name="label",
            name="name",
            field=models.CharField(db_index=True, max_length=100, unique=True),
        ),
    ]
