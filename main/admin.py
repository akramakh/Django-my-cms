from django.contrib import admin
from .models import *
# Register your models here.

class MessageAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email','body')
    search_fields = ('email','firstname',)


admin.site.register(Header)
admin.site.register(Home)
admin.site.register(About)
admin.site.register(Service)
admin.site.register(Portfolio)
admin.site.register(Contact)
admin.site.register(Footer)
admin.site.register(SocialMedia)
admin.site.register(FreelanceAccount)
admin.site.register(Message,MessageAdmin)
