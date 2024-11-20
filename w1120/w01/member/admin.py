from django.contrib import admin
from member.models import Member

class MemberAdmin(admin.ModelAdmin):
  # list_display = ['id','pw','name','nicname','cdate']
  list_display = ['id']

admin.site.register(Member,MemberAdmin)