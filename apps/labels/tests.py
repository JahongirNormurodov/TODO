from django.test import TestCase

from apps.labels.models import Label


class LabelModelTest(TestCase):
    def test_create_label(self):
        label = Label.objects.create(name="Home")

        self.assertEqual(label.name, "Home")
