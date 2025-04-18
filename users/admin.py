from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Users, Order, OrderClosure, Accounting, FilterData


class UserAdmin(BaseUserAdmin):
    list_display = ('login', 'full_name', 'status', 'is_staff', 'is_superuser')
    list_filter = ('status', 'is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('login', 'password')}),
        ('Personal info', {'fields': ('full_name',)}),
        ('Permissions', {'fields': ('status', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('login', 'password1', 'password2', 'full_name', 'status'),
        }),
    )
    search_fields = ('login', 'full_name')
    ordering = ('login',)
    filter_horizontal = ('groups', 'user_permissions',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'client', 'qayerdan', 'qayerga', 'price', 'manager', 'close_order_status')
    list_filter = ('close_order_status', 'manager')
    search_fields = ('order_id', 'client')

admin.site.register(Users, UserAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderClosure)
admin.site.register(Accounting)
admin.site.register(FilterData)