from django.contrib import admin
from panchayatapp.models import waterConection,regesterComplaintes,registerUser,waterApplication
# Register your models here.

# @admin.register(waterConection)
# class waterConectionAdmin(admin.ModelAdmin):
#     list_display = ('name','wardNo','place','houseNo')

@admin.register(regesterComplaintes)
class regesterComplaintesAdmin(admin.ModelAdmin):
    list_display = ('fullName','wardNo','place','complaintes')

@admin.register(registerUser)
class registerUserAdmin(admin.ModelAdmin):
    list_display = ('fullName','wardNo','houseNo')

@admin.register(waterApplication)
class waterApplicationAdmin(admin.ModelAdmin):
    list_display = ('fullName','wardNo','place','houseNo')