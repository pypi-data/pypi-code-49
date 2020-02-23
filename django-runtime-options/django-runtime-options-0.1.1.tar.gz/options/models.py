from django.core.exceptions import ValidationError
from django.db import models


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def is_bool(s):
    return s.lower() in ["true", "false", "1", "0", "t", "f", "y", "n" "yes", "no", "on", "off"]


class Option(models.Model):
    TYPE_TXT = "TXT"
    TYPE_INT = "INT"
    TYPE_BOOL = "BOOL"
    TYPE_CHOICES = ((TYPE_TXT, "Text"), (TYPE_INT, "Integer"), (TYPE_BOOL, "Boolean"))

    key = models.CharField(max_length=255, unique=True)
    value = models.TextField()
    value_type = models.CharField(max_length=8, default=TYPE_TXT, choices=TYPE_CHOICES)

    description = models.TextField(blank=True)

    def as_int(self):
        if self.value_type != self.TYPE_INT:
            return None
        return int(self.value)

    def as_bool(self):
        if self.value_type != self.TYPE_BOOL:
            return None
        return self.value.lower() in ["true", "1", "t", "y", "yes", "on"]

    def __str__(self):
        return f"{self.key}->{self.value}"

    def save(self, *args, **kwargs):
        if self.value_type == self.TYPE_INT:
            if not is_int(self.value):
                raise ValidationError("Type is int but value is not int")
        if self.value_type == self.TYPE_BOOL:
            if not is_bool(self.value):
                raise ValidationError("Type is bool but value is not bool")
        super().save(*args, **kwargs)

    def serialize(self):
        """
        Serialize an option as a dictionary
        """
        return {self.key: self.value}


def get_option(key):
    if Option.objects.filter(key=key).exists():
        return Option.objects.get(key=key)

    return None


def get_value(key, default=None):
    o = get_option(key)
    if o is not None:
        return o.value

    return default


def get_bool(key, default=None):
    o = get_option(key)
    if (o is not None) and (o.value_type == Option.TYPE_BOOL):
        return o.as_bool()

    return default
