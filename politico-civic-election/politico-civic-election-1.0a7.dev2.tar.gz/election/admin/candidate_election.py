# Imports from python.


# Imports from Django.
from django.contrib import admin
from django import forms


# Imports from election.
from election.models import Candidate
from election.models import Election


class CustomModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        if hasattr(obj, "person"):
            return obj.person.full_name
        else:
            return obj.race.label


class CandidateElectionAdminForm(forms.ModelForm):
    candidate = CustomModelChoiceField(queryset=Candidate.objects.all())
    election = CustomModelChoiceField(queryset=Election.objects.all())


class CandidateElectionAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Relationships",
            {
                "fields": (
                    "candidate",
                    "election",
                    "ballot_order",
                    ("aggregable", "uncontested"),
                )
            },
        ),
        ("Identification", {"fields": ("ap_candidate_number",)}),
        ("Record locators", {"fields": ("uid",)}),
    )
    form = CandidateElectionAdminForm
    list_display = ("get_candidate", "get_election", "ballot_order")
    list_select_related = (
        "candidate",
        "candidate__person",
        "election",
        "election__race",
    )
    readonly_fields = ("uid",)
    search_fields = ("candidate__person__full_name", "election__race__label")

    def get_candidate(self, obj):
        return obj.candidate.person.full_name

    get_candidate.short_description = "Candidate"
    get_candidate.admin_order_field = "candidate__person__last_name"

    def get_election(self, obj):
        return obj.election.race.label

    get_election.short_description = "Election"
    get_election.admin_order_field = (
        "election__election_ballot__election_event__election_day__date"
    )
