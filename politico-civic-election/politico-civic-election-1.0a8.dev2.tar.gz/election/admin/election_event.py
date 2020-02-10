# Imports from Django.
from django.contrib import admin


# Imports from election.
from election.models.election_data_url import ElectionDataURL
from election.models.election_type import ElectionType


PRIMARY_TYPE = ElectionType.PARTISAN_PRIMARY


class ElectionDataURLInline(admin.TabularInline):
    model = ElectionDataURL


class ElectionEventAdmin(admin.ModelAdmin):
    list_display = ("get_election_event_name", "get_date")
    list_select_related = ("division", "election_day", "election_type")
    fields = [
        "division",
        "election_day",
        "election_type",
        "election_mode",
        "notes",
    ]
    inlines = [ElectionDataURLInline]
    search_fields = ["division__name", "election_type__slug"]

    def get_election_event_name(self, obj):
        return " ".join(
            [
                f"{obj.division_label}",
                f"{obj.election_type.get_slug_display()}",
            ]
        )

    get_election_event_name.short_description = "Election event"
    get_election_event_name.admin_order_field = "division__slug"

    def get_date(self, obj):
        return obj.election_day.date

    get_date.short_description = "Date"
    get_date.admin_order_field = "election_day__date"
