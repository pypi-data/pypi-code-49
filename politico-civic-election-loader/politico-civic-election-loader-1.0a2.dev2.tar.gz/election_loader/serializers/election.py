# Imports from other dependencies.
from election.models import Candidate
from election.models import CandidateElection
from election.models import Election
from entity.models import Person
from geography.models import Division
from geography.models import DivisionLevel
from government.models import Office
from rest_framework import serializers
import us


class FlattenMixin:
    """
    Flatens the specified related objects in this representation.

    Borrowing this clever method from:
    https://stackoverflow.com/a/41418576/1961614
    """

    def to_representation(self, obj):
        assert hasattr(
            self.Meta, "flatten"
        ), 'Class {serializer_class} missing "Meta.flatten" attribute'.format(
            serializer_class=self.__class__.__name__
        )
        # Get the current object representation
        rep = super(FlattenMixin, self).to_representation(obj)
        # Iterate the specified related objects with their serializer
        for field, serializer_class in self.Meta.flatten:
            try:
                serializer = serializer_class(context=self.context)
                objrep = serializer.to_representation(getattr(obj, field))
                # Include their fields, prefixed, in the current representation
                for key in objrep:
                    rep[key] = objrep[key]
            except Exception:
                continue
        return rep


class DivisionSerializer(serializers.ModelSerializer):
    level = serializers.SerializerMethodField()
    code = serializers.SerializerMethodField()
    parent = serializers.SerializerMethodField()

    def get_level(self, obj):
        """DivisionLevel slug"""
        return obj.level.slug

    def get_code(self, obj):
        if obj.level.name == DivisionLevel.STATE:
            return us.states.lookup(obj.code).abbr
        return obj.code

    def get_parent(self, obj):
        if not obj.parent:
            return None
        if obj.parent.level.name == DivisionLevel.STATE:
            return us.states.lookup(obj.parent.code).abbr
        return obj.code

    class Meta:
        model = Division
        fields = ("code", "level", "parent")


class PersonSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    def get_images(self, obj):
        """Object of images serialized by tag name."""
        return {str(i.tag): i.image.url for i in obj.images.all()}

    class Meta:
        model = Person
        fields = ("first_name", "middle_name", "last_name", "suffix", "images")


class CandidateSerializer(FlattenMixin, serializers.ModelSerializer):
    party = serializers.SerializerMethodField()

    def get_party(self, obj):
        """Party AP code."""
        return obj.party.ap_code

    class Meta:
        model = Candidate
        fields = ("party", "ap_candidate_id", "incumbent", "uid")
        flatten = (("person", PersonSerializer),)


class CandidateElectionSerializer(FlattenMixin, serializers.ModelSerializer):
    class Meta:
        model = CandidateElection
        fields = ("aggregable", "uncontested")
        flatten = (("candidate", CandidateSerializer),)


class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = ("uid", "slug", "name", "label", "short_label")


class ElectionSerializer(serializers.ModelSerializer):
    primary = serializers.SerializerMethodField()
    primary_party = serializers.SerializerMethodField()
    runoff = serializers.SerializerMethodField()
    special = serializers.SerializerMethodField()
    office = serializers.SerializerMethodField()
    candidates = CandidateSerializer(many=True, read_only=True)
    date = serializers.SerializerMethodField()
    division = DivisionSerializer()
    candidates = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    def get_candidates(self, obj):
        """
        CandidateElections.
        """
        return CandidateElectionSerializer(
            obj.candidate_elections.all(), many=True
        ).data

    def get_primary(self, obj):
        """
        If primary
        """
        return obj.election_type.is_primary()

    def get_primary_party(self, obj):
        """
        If primary, party AP code.
        """
        if obj.party:
            return obj.party.ap_code
        return None

    def get_runoff(self, obj):
        """
        If runoff
        """
        return obj.election_type.is_runoff()

    def get_special(self, obj):
        """
        If special
        """
        return obj.race.special

    def get_office(self, obj):
        """Office candidates are running for."""
        return OfficeSerializer(obj.race.office).data

    def get_date(self, obj):
        """Election date."""
        return obj.election_day.date

    def get_description(self, obj):
        return obj.race.description

    class Meta:
        model = Election
        fields = (
            "uid",
            "date",
            "office",
            "primary",
            "primary_party",
            "runoff",
            "special",
            "division",
            "candidates",
            "description",
            "ap_election_id",
        )
