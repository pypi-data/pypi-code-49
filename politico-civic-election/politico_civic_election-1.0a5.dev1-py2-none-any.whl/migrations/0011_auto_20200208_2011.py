# Generated by Django 3.0.2 on 2020-02-08 20:11

from django.db import migrations
from django.utils import timezone


# Really, really dumb that these can't be referenced from the class.
ALL_PARTY_PRIMARY_TYPE = "all-party-primary"
TOP_TWO_PRIMARY_TYPE = "top-two-primary"
MAJORITY_ELECTS_BLANKET_PRIMARY_TYPE = "majority-elects-blanket-primary"


def split_all_party_primary_instances(apps, schema_editor):
    """We want to delete the vague "All-party primary" type.

    To do this, we need to reassign election events with this value to
    two more specific types:

        - "Top-two" primaries, which are mainly held in CA and WA, and
        - "Majority-elects" primaries, mostly held in the south.

    You can read more about each type of primary in this app's
    models.py file.

    We split this based on state postal code -- meaning election events
    that are at non-state levels will raise an error.

    This is preferred, as that's an edge case outside current scope.
    """
    ElectionEvent = apps.get_model("election", "ElectionEvent")
    ElectionType = apps.get_model("election", "ElectionType")

    events_to_modify = ElectionEvent.objects.filter(
        election_type__slug=ALL_PARTY_PRIMARY_TYPE
    )

    if events_to_modify:
        top_two_type, created = ElectionType.objects.get_or_create(
            slug=TOP_TWO_PRIMARY_TYPE,
            defaults=dict(created=timezone.now(), updated=timezone.now()),
        )

        majority_elects_type, created = ElectionType.objects.get_or_create(
            slug=MAJORITY_ELECTS_BLANKET_PRIMARY_TYPE,
            defaults=dict(created=timezone.now(), updated=timezone.now()),
        )

        for election_event in events_to_modify:
            if election_event.division.code_components["postal"] in [
                "CA",
                "WA",
            ]:
                new_election_type = top_two_type
            else:
                new_election_type = majority_elects_type

            election_event.election_type = new_election_type
            election_event.save()


def remerge_all_party_primary_instances(apps, schema_editor):
    """Reversing migration: Join the more descriptive types to one.

    When reversing this migration, recast all instances with election
    types of "Top-two" or "Majority-elects blanket" primaries back to
    the old, vague "All-party primary" election type.
    """
    ElectionEvent = apps.get_model("election", "ElectionEvent")
    ElectionType = apps.get_model("election", "ElectionType")

    top_two_events = ElectionEvent.objects.filter(
        election_type__slug=TOP_TWO_PRIMARY_TYPE
    )
    majority_elects_events = ElectionEvent.objects.filter(
        election_type__slug=MAJORITY_ELECTS_BLANKET_PRIMARY_TYPE
    )

    if top_two_events or majority_elects_events:
        all_party_type, created = ElectionType.objects.get_or_create(
            slug=ALL_PARTY_PRIMARY_TYPE,
            defaults=dict(created=timezone.now(), updated=timezone.now()),
        )

        for election_event in top_two_events:
            election_event.election_type = all_party_type
            election_event.save()

        for election_event in majority_elects_events:
            election_event.election_type = all_party_type
            election_event.save()


class Migration(migrations.Migration):

    dependencies = [("election", "0010_auto_20200208_2010")]

    operations = [
        migrations.RunPython(
            split_all_party_primary_instances,
            remerge_all_party_primary_instances,
        )
    ]
