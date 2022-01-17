from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *
from ckeditor_uploader.widgets  import CKEditorUploadingWidget 
from django import forms

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget ())
    class Meta:
        model = Block
        fields = '__all__'

class TegAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ('title', )}



class BlockAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ('title', )}
    form =PostAdminForm
    save_as = True
    list_display = ('title', 'category', 'created_at', 'view', 'slug', 'get_photo')
    list_display_links = ('title', 'category')
    #block page search qatori
    search_fields = ('title',)
    #block page filter qatori
    list_filter = ('category', 'tag',)

    #admin panel block page rasm qatori
    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width='50'>")
        else:
            return '--'

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ('title', )}



admin.site.register(Block, BlockAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Teg, TegAdmin)