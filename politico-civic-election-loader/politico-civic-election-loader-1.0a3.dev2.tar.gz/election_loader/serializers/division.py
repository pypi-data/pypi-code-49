# Imports from other dependencies.
from geography.models import Division
from rest_framework import serializers
import us


class ChildDivisionSerializer(serializers.ModelSerializer):
    level = serializers.SerializerMethodField()
    postal_code = serializers.SerializerMethodField()

    def get_postal_code(self, obj):
        if obj.level.name == "state":
            return us.states.lookup(obj.code).abbr
        return None

    def get_level(self, obj):
        return obj.level.slug

    class Meta:
        model = Division
        fields = (
            "label",
            "short_label",
            "code",
            "code_components",
            "postal_code",
            "level",
        )


class DivisionSerializer(ChildDivisionSerializer):
    children = serializers.SerializerMethodField()

    def get_children(self, obj):
        kwargs = {}

        if self.context.get("children_level"):
            kwargs["level__name"] = self.context.get("children_level")

        return ChildDivisionSerializer(
            obj.children.filter(**kwargs), many=True, read_only=True
        ).data

    class Meta:
        model = Division
        fields = (
            "uid",
            "label",
            "short_label",
            "code",
            "level",
            "code_components",
            "postal_code",
            "children",
        )
