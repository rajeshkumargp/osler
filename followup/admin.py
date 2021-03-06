from __future__ import unicode_literals
from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from pttrack.admin import NoteAdmin
from . import models


for model in [models.NoShowReason, models.NoAptReason, models.ContactResult]:
    if hasattr(model, "history"):
        admin.site.register(model, SimpleHistoryAdmin)
    else:
        admin.site.register(model)

for model in [models.LabFollowup, models.VaccineFollowup,
              models.GeneralFollowup, models.ReferralFollowup]:
    admin.site.register(model, NoteAdmin)
