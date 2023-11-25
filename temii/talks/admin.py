from django.contrib import admin

from .models import Talk


@admin.register(Talk)
class TalkAdmin(admin.ModelAdmin):
    list_display = ["name", "user", "months"]
    search_fields = ["name"]
    list_filter = ["level", "precense", "language"]
