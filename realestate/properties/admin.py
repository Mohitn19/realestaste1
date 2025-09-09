from django.contrib import admin
from .models import Property

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'property_type', 'status', 'price', 'city', 'state', 'created_at')
    list_filter = ('property_type', 'status', 'city', 'state', 'created_at')
    search_fields = ('title', 'description', 'address', 'city', 'state')
    list_editable = ('status',)
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'property_type', 'status')
        }),
        ('Property Details', {
            'fields': ('price', 'bedrooms', 'bathrooms', 'area')
        }),
        ('Location', {
            'fields': ('address', 'city', 'state', 'zip_code')
        }),
        ('Media', {
            'fields': ('image',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
