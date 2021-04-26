from django.contrib import admin
from .models import Product
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget



class ProductAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Product
        fields = '__all__'


class ProductAdmin(admin.ModelAdmin):
	list_display = ('id','name','category')
	list_display_links = ('id','name')
	search_fields = ('name',)
	list_filter = ('name','category')
	form = ProductAdminForm


admin.site.register(Product,ProductAdmin)
