from django.contrib import admin

from .models import Question, Choice

# Register your models here.



class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3 
    
class QuestionAdmin(admin.ModelAdmin):
    # fields = ["pub_date", "question_text"]
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date info", {"fields": ["pub_date"]})
    ]

    inlines = [ChoiceInline]

    list_display = ["question_text", "pub_date", "was_published_recently"]

    list_filter = ["pub_date"]

    search_fields = ["question_text"]


admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice)

admin.site.site_header = "Super Admin"

class MyAdminSite(admin.AdminSite):
    site_header = 'Poll Admin'

my_admin_site = MyAdminSite(name = 'myadmin')
my_admin_site.register(Question, QuestionAdmin)
my_admin_site.register(Choice)
