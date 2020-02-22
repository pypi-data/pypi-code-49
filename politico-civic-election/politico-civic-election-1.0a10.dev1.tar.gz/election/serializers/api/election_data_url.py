# Imports from other dependencies.
from civic_utils.serializers import CommandLineListSerializer


# Imports from election.
from election.models import ElectionDataURL


class ElectionDataURLAPISerializer(CommandLineListSerializer):
    class Meta(CommandLineListSerializer.Meta):
        model = ElectionDataURL
        fields = ("url_descriptor", "url_path")
