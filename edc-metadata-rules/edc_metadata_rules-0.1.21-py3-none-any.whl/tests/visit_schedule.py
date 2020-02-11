from dateutil.relativedelta import relativedelta

from edc_visit_schedule import VisitSchedule, Schedule, Visit
from edc_visit_schedule import FormsCollection, Crf, Requisition
from edc_visit_schedule.tests import DummyPanel


app_label = "edc_metadata_rules"


class MockPanel(DummyPanel):
    """`requisition_model` is normally set when the lab profile
    is set up.
    """

    def __init__(self, name):
        super().__init__(
            requisition_model="edc_metadata_rules.subjectrequisition", name=name
        )


crfs0 = FormsCollection(
    Crf(show_order=1, model=f"{app_label}.crfone", required=True),
    Crf(show_order=2, model=f"{app_label}.crftwo", required=True),
    Crf(show_order=3, model=f"{app_label}.crfthree", required=True),
    Crf(show_order=4, model=f"{app_label}.crffour", required=True),
    Crf(show_order=5, model=f"{app_label}.crffive", required=True),
)

crfs1 = FormsCollection(
    Crf(show_order=1, model=f"{app_label}.crffour", required=True),
    Crf(show_order=2, model=f"{app_label}.crffive", required=True),
    Crf(show_order=3, model=f"{app_label}.crfsix", required=True),
)

crfs2 = FormsCollection(Crf(show_order=1, model=f"{app_label}.crfseven", required=True))


requisitions0 = FormsCollection(
    Requisition(
        show_order=10, panel=MockPanel("one"), required=False, additional=False
    ),
    Requisition(
        show_order=20, panel=MockPanel("two"), required=False, additional=False
    ),
    Requisition(
        show_order=30, panel=MockPanel("three"), required=False, additional=False
    ),
    Requisition(
        show_order=40, panel=MockPanel("four"), required=False, additional=False
    ),
    Requisition(
        show_order=50, panel=MockPanel("five"), required=False, additional=False
    ),
    Requisition(
        show_order=60, panel=MockPanel("six"), required=False, additional=False
    ),
)

requisitions1 = FormsCollection(
    Requisition(
        show_order=10, panel=MockPanel("four"), required=False, additional=False
    ),
    Requisition(
        show_order=20, panel=MockPanel("five"), required=False, additional=False
    ),
    Requisition(
        show_order=30, panel=MockPanel("six"), required=False, additional=False
    ),
    Requisition(
        show_order=40, panel=MockPanel("seven"), required=False, additional=False
    ),
    Requisition(
        show_order=50, panel=MockPanel("eight"), required=False, additional=False
    ),
    Requisition(
        show_order=60, panel=MockPanel("nine"), required=False, additional=False
    ),
)


requisitions2 = FormsCollection(
    Requisition(
        show_order=10, panel=MockPanel("seven"), required=False, additional=False
    )
)

visit0 = Visit(
    code="1000",
    title="Day 1",
    timepoint=0,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=6),
    requisitions=requisitions0,
    crfs=crfs0,
    facility_name="default",
)

visit1 = Visit(
    code="2000",
    title="Day 2",
    timepoint=1,
    rbase=relativedelta(days=1),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=6),
    requisitions=requisitions1,
    crfs=crfs1,
    facility_name="default",
)

visit2 = Visit(
    code="3000",
    title="Day 3",
    timepoint=2,
    rbase=relativedelta(days=2),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=6),
    requisitions=requisitions2,
    crfs=crfs2,
    facility_name="default",
)

schedule = Schedule(
    name="schedule",
    onschedule_model=f"{app_label}.onschedule",
    offschedule_model=f"{app_label}.offschedule",
    consent_model=f"{app_label}.subjectconsent",
    appointment_model="edc_appointment.appointment",
)

schedule.add_visit(visit0)
schedule.add_visit(visit1)
schedule.add_visit(visit2)

visit_schedule = VisitSchedule(
    name="visit_schedule",
    offstudy_model=f"{app_label}.subjectoffstudy",
    death_report_model=f"{app_label}.deathreport",
)

visit_schedule.add_schedule(schedule)
