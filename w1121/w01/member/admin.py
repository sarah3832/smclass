from django.contrib import admin
from member.models import Member

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
  list_display = ['id','name','nickname','mdate']

## 관리자페이지 컬럼 보이기 (골뱅이로 대체가능)
# admin.site.register(Member,MemberAdmin)