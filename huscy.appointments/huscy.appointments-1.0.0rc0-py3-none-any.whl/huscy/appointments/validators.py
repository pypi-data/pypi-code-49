from huscy.appointments.models import Resource


def validate_start_end(start, end):
    if start > end:
        raise ValueError("End must be greater then start.")
    elif start == end:
        raise ValueError("Start and end are the same.")


def validate_resource_exists(resource):
    if resource and not Resource.objects.filter(name=resource).exists():
        raise ValueError(f'Resource: {resource} does not exist')
