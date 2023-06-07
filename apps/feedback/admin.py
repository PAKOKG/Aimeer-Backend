from django.contrib import admin

from .models import Feedback, ConnectWithUs


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    ...


@admin.register(ConnectWithUs)
class ConnectWithUsAdmin(admin.ModelAdmin):
    ...
