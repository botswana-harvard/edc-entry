from django.db import models

from edc.subject.entry.choices import ENTRY_CATEGORY, ENTRY_WINDOW, ENTRY_STATUS
from edc.subject.visit_schedule.models import BaseWindowPeriodItem
from edc.subject.visit_schedule.models import VisitDefinition

from ..exceptions import EntryManagerError
from ..managers import LabEntryManager
from edc.constants import NOT_REQUIRED, REQUIRED

from .requisition_panel import RequisitionPanel


class LabEntry(BaseWindowPeriodItem):

    visit_definition = models.ForeignKey(VisitDefinition)

    requisition_panel = models.ForeignKey(RequisitionPanel, null=True)

    app_label = models.CharField(max_length=50, null=True, help_text='requisition_panel app_label')

    model_name = models.CharField(max_length=50, null=True, help_text='requisition_panel model_name')

    entry_order = models.IntegerField()

    entry_category = models.CharField(
        max_length=25,
        choices=ENTRY_CATEGORY,
        default='CLINIC',
        )

    entry_window_calculation = models.CharField(
        max_length=25,
        choices=ENTRY_WINDOW,
        default='VISIT',
        help_text=('Base the entry window period on the visit window period '
                   'or specify a form specific window period'),
        )

    default_entry_status = models.CharField(
        max_length=25,
        choices=ENTRY_STATUS,
        default=REQUIRED,
        )

    additional = models.BooleanField(
        default=False,
        help_text='If True lists the lab_entry in additional requisitions')

    objects = LabEntryManager()

    def save(self, *args, **kwargs):
        model = models.get_model(self.app_label, self.model_name)
        if not model:
            raise TypeError('Lab Entry \'{2}\' cannot determine requisition_panel model '
                            'from app_label=\'{0}\' and model_name=\'{1}\''.format(
                                self.app_label, self.model_name, self))
        try:
            model.entry_meta_data_manager
        except AttributeError:
            raise EntryManagerError('Models linked by the LabEntry class require a meta data manager. '
                                    'Add entry_meta_data_manager=RequisitionMetaDataManager() to '
                                    'model {0}.{1}'.format(self.app_label, self.model_name))
        super(LabEntry, self).save(*args, **kwargs)

    def natural_key(self):
        return self.visit_definition.natural_key() + self.requisition_panel.natural_key()

    def get_model(self):
        return models.get_model(self.app_label, self.model_name)

    def form_title(self):
        self.content_type_map.content_type.model_class()._meta.verbose_name

    def __unicode__(self):
        return '{0}.{1}'.format(self.visit_definition.code, self.requisition_panel.name)

    @property
    def required(self):
        return self.default_entry_status != NOT_REQUIRED

    @property
    def not_required(self):
        return not self.required

    class Meta:
        app_label = 'entry'
        verbose_name = "Lab Entry"
        ordering = ['visit_definition__code', 'entry_order', ]
        unique_together = ['visit_definition', 'requisition_panel', ]
