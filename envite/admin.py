from django.contrib import admin

# Register your models here.
from .models import SeatingTable, SeatingGuest

class SeatingGuestInline(admin.TabularInline):
    model = SeatingGuest
    extra = 1

@admin.register(SeatingTable)
class SeatingTableAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity', 'guest_count', 'order')
    inlines = [SeatingGuestInline]

    def guest_count(self, obj):
        return obj.guest_count()

@admin.register(SeatingGuest)
class SeatingGuestAdmin(admin.ModelAdmin):
    list_display = ('name', 'table', 'seat')
    search_fields = ('name',)