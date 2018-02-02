from django.contrib import admin
from d21.election.models import Election


@admin.register(Election)
class ElectionAdmin(admin.ModelAdmin):
    # TODO: create choice inline
    pass
