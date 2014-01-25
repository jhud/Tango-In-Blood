from django.contrib import admin
from tango_in_blood_app.models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'avatar', 'conversion_password', 'converted_by')
    fields = ('user', 'bio', 'avatar', 'conversion_password', 'converted_by')
    #readonly_fields = ('user',)
    
admin.site.register(Profile, ProfileAdmin)