from django.contrib import admin
from .models import Site, SiteMap


class SiteAdmin(admin.ModelAdmin):
    list_display = ('pk', 'url', 'created_at',)
    search_fields = ('url',)
    list_filter = ('created_at',)


class SiteMapAdmin(admin.ModelAdmin):
    list_display = ('pk', 'url', 'created_at', 'site',)
    search_fields = ('url',)
    list_filter = ("site",)


admin.site.register(Site, SiteAdmin)
admin.site.register(SiteMap, SiteMapAdmin)