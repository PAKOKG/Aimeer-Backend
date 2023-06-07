from django.contrib import admin

from .models import Product, Resume, Certificate


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ...


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    ...


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    ...
