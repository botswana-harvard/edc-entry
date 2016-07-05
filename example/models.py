from django.db import models

from edc_appointment.mixins import AppointmentModelMixin
from edc_base.model.models.base_uuid_model import BaseUuidModel
from edc_meta_data.crf_meta_data_managers import CrfMetaDataManager
from edc_meta_data.crf_meta_data_mixin import CrfMetaDataMixin
from edc_registration.models import RegisteredSubjectModelMixin
from edc_visit_tracking.models.crf_model_mixin import CrfModelMixin
from edc_visit_tracking.models.previous_visit_mixin import PreviousVisitMixin
from edc_visit_tracking.models.visit_model_mixin import VisitModelMixin


class RegisteredSubject(RegisteredSubjectModelMixin):

    class Meta:
        app_label = 'example'


class Appointment(AppointmentModelMixin, BaseUuidModel):

    registered_subject = models.ForeignKey(RegisteredSubject)

    class Meta:
        app_label = 'example'


class SubjectVisit(CrfMetaDataMixin, PreviousVisitMixin, VisitModelMixin, BaseUuidModel):

    appointment = models.OneToOneField(Appointment)

    class Meta:
        app_label = 'example'


class CrfOne(CrfModelMixin, BaseUuidModel):

    subject_visit = models.ForeignKey(SubjectVisit)

    f1 = models.CharField(max_length=10, default='erik')

    entry_meta_data_manager = CrfMetaDataManager(SubjectVisit)

    class Meta:
        app_label = 'example'
