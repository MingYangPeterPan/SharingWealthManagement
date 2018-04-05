from django.contrib import admin
from UserModel.models import User, Contact, Tag

# Register your models here.
class TagInline(admin.TabularInline):
    model = Tag

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email')  # list
    search_fields = ('name',)
    inlines = [TagInline]  # Inline
    fieldsets = (
        ['Main', {
            'fields': ('name', 'email'),
        }],
        ['Advance', {
            'classes': ('collapse',),  # CSS
            'fields': ('age',),
        }]
    )
    #fields = ('name', 'email')

# Register your models here.
admin.site.register(Contact, ContactAdmin)
admin.site.register([User, Tag])

