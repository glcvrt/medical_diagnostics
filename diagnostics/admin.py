from django.contrib import admin

from diagnostics.models import Directions, Doctor, Diagnostic, Review


@admin.register(Directions)
class DirectionsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('fio', 'experience', 'directions', 'add_info',)
    list_filter = ('directions',)


@admin.register(Diagnostic)
class DiagnosticAdmin(admin.ModelAdmin):
    list_display = ('title', 'price',)
    list_filter = ('price', 'doctor',)
    search_fields = ('title', 'price', 'doctor',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('text', 'user',)
    list_filter = ('user',)


