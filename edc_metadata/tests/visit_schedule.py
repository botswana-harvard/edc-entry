from dateutil.relativedelta import relativedelta

from edc_visit_schedule import VisitSchedule, Schedule, Visit
from edc_visit_schedule import FormsCollection, Crf, Requisition


app_label = 'edc_metadata'

crfs0 = FormsCollection(
    Crf(show_order=1, model=f'{app_label}.crfone', required=True),
    Crf(show_order=2, model=f'{app_label}.crftwo', required=True),
    Crf(show_order=3, model=f'{app_label}.crfthree', required=True),
    Crf(show_order=4, model=f'{app_label}.crffour', required=True),
    Crf(show_order=5, model=f'{app_label}.crffive', required=True),
)

crfs1 = FormsCollection(
    Crf(show_order=1, model=f'{app_label}.crffour', required=True),
    Crf(show_order=2, model=f'{app_label}.crffive', required=True),
    Crf(show_order=3, model=f'{app_label}.crfsix', required=True),
)

crfs2 = FormsCollection(
    Crf(show_order=1, model=f'{app_label}.crfseven', required=True),
)

requisitions = FormsCollection(
    Requisition(
        show_order=10, model='edc_metadata.subjectrequisition',
        panel='one', required=True, additional=False),
    Requisition(
        show_order=20, model='edc_metadata.subjectrequisition',
        panel='two', required=True, additional=False),
    Requisition(
        show_order=30, model='edc_metadata.subjectrequisition',
        panel='three', required=True, additional=False),
    Requisition(
        show_order=40, model='edc_metadata.subjectrequisition',
        panel='four', required=True, additional=False),
    Requisition(
        show_order=50, model='edc_metadata.subjectrequisition',
        panel='five', required=True, additional=False),
    Requisition(
        show_order=60, model='edc_metadata.subjectrequisition',
        panel='six', required=True, additional=False),
)

requisitions3000 = FormsCollection(
    Requisition(
        show_order=10, model='edc_metadata.subjectrequisition',
        panel='seven', required=True, additional=False),
)

visit0 = Visit(
    code='1000',
    title='Day 1',
    timepoint=0,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=6),
    requisitions=requisitions,
    crfs=crfs0)

visit1 = Visit(
    code='2000',
    title='Day 2',
    timepoint=1,
    rbase=relativedelta(days=1),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=6),
    requisitions=requisitions,
    crfs=crfs1)

visit2 = Visit(
    code='3000',
    title='Day 3',
    timepoint=2,
    rbase=relativedelta(days=2),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=6),
    requisitions=requisitions3000,
    crfs=crfs2)

schedule = Schedule(
    name='schedule',
    enrollment_model='edc_metadata.enrollment',
    disenrollment_model='edc_metadata.disenrollment')

schedule.add_visit(visit0)
schedule.add_visit(visit1)
schedule.add_visit(visit2)

visit_schedule = VisitSchedule(
    name='visit_schedule',
    visit_model='edc_metadata.subjectvisit',
    offstudy_model='edc_metadata.subjectoffstudy')

visit_schedule.add_schedule(schedule)
