# Imports from Django.
from django.contrib import admin
from django.utils.translation import gettext_lazy as _


# Imports from other dependencies.
from government.models import Jurisdiction
from government.models import Party


# Imports from election.
from election.models import ElectionCycle


class CycleFilter(admin.SimpleListFilter):
    title = _("cycle")
    parameter_name = "cycle"

    def lookups(self, request, model_admin):
        return [
            (cycle.slug, _(cycle.name))
            for cycle in ElectionCycle.objects.all()
        ]

    def queryset(self, request, queryset):
        if not self.value():
            return queryset
        return queryset.filter(cycle__name=self.value())


class JurisdictionFilter(admin.SimpleListFilter):
    title = _("jurisdiction")
    parameter_name = "jurisdiction"

    def lookups(self, request, model_admin):
        return [
            (jurisdiction.slug, _(jurisdiction.name))
            for jurisdiction in Jurisdiction.objects.all()
        ]

    def queryset(self, request, queryset):
        if not self.value():
            return queryset
        return queryset.filter(office__jurisdiction__slug=self.value())


class PartyFilter(admin.SimpleListFilter):
    title = _("party")
    parameter_name = "party"

    def lookups(self, request, model_admin):
        return [
            (party.ap_code, _(party.__str__()))
            for party in Party.objects.all()
        ]

    def queryset(self, request, queryset):
        if not self.value():
            return queryset
        return queryset.filter(party__ap_code=self.value())


class CandidateAdmin(admin.ModelAdmin):
    list_display = ("get_person", "get_cycle", "get_office", "get_party")
    list_filter = (CycleFilter, JurisdictionFilter, PartyFilter)
    list_select_related = ("party", "person")
    readonly_fields = ("uid",)
    search_fields = ("person__full_name",)

    # ap_candidate_id

    fieldsets = (
        (
            "Relationships",
            {
                "fields": (
                    "person",
                    "party",
                    "cycle",
                    "office",
                    "top_of_ticket",
                )
            },
        ),
        (
            "Identification",
            {"fields": ("ap_candidate_id", "incumbent", "prospective")},
        ),
        ("Record locators", {"fields": ("uid",)}),
    )

    def get_person(self, obj):
        return obj.person.full_name

    get_person.short_description = "Name"
    get_person.admin_order_field = "person__full_name"

    def get_cycle(self, obj):
        return obj.cycle.name

    get_cycle.short_description = "Cycle"
    get_cycle.admin_order_field = "cycle__name"

    def get_office(self, obj):
        return obj.office

    get_office.short_description = "Office"
    get_office.admin_order_field = "office"

    def get_party(self, obj):
        return obj.party.label

    get_party.short_description = "Party"
    get_party.admin_order_field = "party__label"
