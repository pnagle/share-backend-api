from django.contrib import admin

from .models import Users,Events,NGOS,News,Company,Volunteers,Causes,Runs,Partners,Sponsors,CausesCategory,CompanyCategory,SponsorType


admin.site.register(Users)
admin.site.register(Events)
admin.site.register(Volunteers)
admin.site.register(Company)
admin.site.register(News)
admin.site.register(NGOS)
admin.site.register(Causes)
admin.site.register(Runs)
admin.site.register(Partners)
admin.site.register(Sponsors)
admin.site.register(CausesCategory)
admin.site.register(CompanyCategory)
admin.site.register(SponsorType)
