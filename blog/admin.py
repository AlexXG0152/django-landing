# Register your models here.
from django.contrib import admin
from .models import Post
from .models import Feedback
from django_summernote.admin import SummernoteModelAdmin


class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number','date',)
    search_fields = ('name', 'email',)
    date_hierarchy = 'date'

admin.site.register(Post, SomeModelAdmin)
admin.site.register(Feedback, FeedbackAdmin)
