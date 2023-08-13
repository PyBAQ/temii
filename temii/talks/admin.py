from django.contrib import admin

from .models import Talk, TalkLanguage, TalkLevel


@admin.register(Talk)
class TalkAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


@admin.register(TalkLanguage)
class TalkLanguageAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


@admin.register(TalkLevel)
class TalkLevelAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
