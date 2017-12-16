from django.contrib import admin
from .models import Product
# Register your models here
# admin.site.register(Product)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'main', 'time')  # list
    search_fields = ('title',)
    fields = ('title', 'author', 'time', 'main', 'content')

    class Media:
        js = (
            '/static/kindeditor-4.1.10/kindeditor-min.js',
            '/static/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/kindeditor-4.1.10/config.js',
        )

admin.site.site_header = 'Touch管理系统'
admin.site.site_title = '后台管理'