from django.db import models


class TestModel(models.Model):
    test_field = models.CharField(
        max_length=255,
        verbose_name="Foo verbose name",
        help_text="Foo help_text",
    )
