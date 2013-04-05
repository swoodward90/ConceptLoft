from django.contrib import admin
from contest.models import *

admin.site.register(Company)
admin.site.register(UserProfile)
admin.site.register(Contest)
admin.site.register(Entry)
admin.site.register(Distribution)