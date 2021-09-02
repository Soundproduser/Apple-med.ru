from django import forms
from django.contrib import admin

from .models import *


class MedicationCategoryChoiceField(forms.ModelChoiceField):
    pass


class MedicationAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return MedicationCategoryChoiceField(Category.objects.filter(slug='Medication'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)



class VitaminAndMineralCategoryChoiceField(forms.ModelChoiceField):
    pass


class VitaminAndMineralAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return MedicationCategoryChoiceField(Category.objects.filter(slug='VitaminAndMineral'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(Medication, MedicationAdmin)
admin.site.register(VitaminAndMineral, VitaminAndMineralAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
