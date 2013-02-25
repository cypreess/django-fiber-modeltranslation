from django.contrib import admin
from fiber import fiber_admin

from fiber.models import Page, ContentItem
from fiber.admin import PageAdmin, ContentItemAdmin
from fiber.admin import FiberAdminContentItemAdmin, FiberAdminPageAdmin

from modeltranslation.admin import TranslationAdmin


class CustomPageAdmin(TranslationAdmin, PageAdmin):
    pass

class CustomContentItemAdmin(TranslationAdmin, ContentItemAdmin):
    pass


class CustomFiberAdminPageAdmin(TranslationAdmin, FiberAdminPageAdmin):
    pass


class CustomFiberAdminContentItemAdmin(TranslationAdmin, FiberAdminContentItemAdmin):
    pass


admin.site.unregister(Page)
admin.site.unregister(ContentItem)

fiber_admin.site.unregister(ContentItem)
fiber_admin.site.unregister(Page)

admin.site.register(Page, CustomPageAdmin)
admin.site.register(ContentItem, CustomContentItemAdmin)
fiber_admin.site.register(Page, CustomFiberAdminPageAdmin)
fiber_admin.site.register(ContentItem, CustomFiberAdminContentItemAdmin)
