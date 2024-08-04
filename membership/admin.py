from django.contrib import admin
from .models import Family, MemberStatus, Member
# Register your models here.
admin.site.register(Family)
admin.site.register(MemberStatus)
admin.site.register(Member)

#class MemberAdmin(admin.ModelAdmin):
#    list_display = ('user', 'client', 'join_date', 'status', 'email', 'phone_number')
#    search_fields = ('user__email', 'client__name')
#    list_filter = ('status', 'client')
#admin.site.register(Member, MemberAdmin)
