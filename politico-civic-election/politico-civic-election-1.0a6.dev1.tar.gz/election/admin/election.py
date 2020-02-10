# Imports from Django.
from django.contrib import admin
from django import forms


# Imports from election.
from election.models import CandidateElection


class CustomModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        if hasattr(obj, "name"):
            return obj.name
        elif hasattr(obj, "date"):
            return obj.date
        else:
            return obj.label


class CandidateElectionInline(admin.StackedInline):
    model = CandidateElection
    extra = 0


class ElectionAdmin(admin.ModelAdmin):
    list_display = (
        "get_office",
        "election_date",
        "get_election_type",
        "get_party",
        "special",
    )
    list_filter = (
        "election_ballot__election_event__election_day__date",
        "race__special",
        "election_ballot__election_event__election_type__label",
    )
    list_select_related = (
        "election_ballot",
        "election_ballot__election_event",
        "election_ballot__election_event__election_day",
        "election_ballot__election_event__election_type",
        "race",
        "race__office",
    )
    ordering = (
        "election_ballot__election_event__election_day__date",
        "election_ballot__election_event__division__label",
        "election_ballot__party__label",
    )
    search_fields = (
        "race__label",
        "election_ballot__election_event__election_day__date",
        "election_ballot__election_event__election_day__slug",
    )
    autocomplete_fields = ["race"]
    inlines = [CandidateElectionInline]
    readonly_fields = ("uid",)
    fieldsets = (
        (
            "Relationships",
            {"fields": ("election_ballot", "race", "ap_election_id")},
        ),
        ("Record locators", {"fields": ("uid",)}),
    )

    def get_office(self, obj):
        return obj.race.office.label

    def election_date(self, obj):
        return obj.election_ballot.election_event.election_day.date

    def get_election_type(self, obj):
        return obj.election_ballot.election_event.election_type.label

    def get_party(self, obj):
        if obj.election_ballot.party:
            return obj.election_ballot.party.label
        else:
            return None

    def special(self, obj):
        return obj.race.special

    get_office.short_description = "Office"
    get_election_type.short_description = "Election Type"
    get_party.short_description = "Primary Party"
