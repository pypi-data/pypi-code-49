"""

The randomisation of the 32 health facilities will be stratified by country and
type of health facility (defined by the infrastructure available) and by
size of health facility. Within each stratum, we will randomise in a 1:1 ratio
to either immediate or deferred using a computer-generated randomisation list.

As mentioned above, the 32 facilities chosen will be chosen purposely such
that their catchment populations are separated by natural barriers so as
to minimise contamination (e.g. persons living in control areas travelling
to intervention facilities for health care).


"""
from edc_auth.codenames.clinic import clinic


INTERMEDIATE = "immediate"
DEFFERED = "deferred"


class Clinic:
    def __init__(
        self,
        town=None,
        district=None,
        region=None,
        health_facility_type=None,
        attendance_per_month=None,
    ):
        pass
