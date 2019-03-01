from django.contrib import admin

from .models import Choice, Attribute, AttributeValue, Event, Group
from .models import Organization, MainOrganization, Member, MenuLine


class AttributeValueInline(admin.TabularInline):
    model = AttributeValue
    fields = ["attribute", "value"]


class MemberAdmin(admin.ModelAdmin):
    inlines = [
        AttributeValueInline,
    ]


class EventAdmin(admin.ModelAdmin):
    inlines = [
        AttributeValueInline,
    ]


class GroupAdmin(admin.ModelAdmin):
    inlines = [
        AttributeValueInline,
    ]


class OrganizationAdmin(admin.ModelAdmin):
    inlines = [
        AttributeValueInline,
    ]


class MainOrganizationAdmin(admin.ModelAdmin):
    inlines = [
        AttributeValueInline,
    ]


admin.site.register(Choice)
admin.site.register(Attribute)
admin.site.register(AttributeValue)
admin.site.register(Event, EventAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(MainOrganization, MainOrganizationAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(MenuLine)