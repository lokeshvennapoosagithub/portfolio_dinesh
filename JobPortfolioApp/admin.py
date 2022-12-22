from django.contrib import admin

from JobPortfolioApp.models import Data, Service, RecentWork,Client
# Register your models here.
admin.site.register(Data)
admin.site.register(Service)
admin.site.register(RecentWork)
admin.site.register(Client)