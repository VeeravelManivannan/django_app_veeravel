from django.contrib import admin
from .models import Question,Choice



#For Inline choice model(ie editing both the PARENT and CHILD model in the same admin page)
class ChoiceInLine(admin.TabularInline):
    model = Choice

#Decorator for model.was_published_recently
def decorateWasPublishedRecently(obj):
    return obj.was_published_recently()
decorateWasPublishedRecently.short_description = 'PUBLISHED RECENTLY ?'


#Modeladmins
class QuestionAdmin(admin.ModelAdmin):

    #PS 'fields' expects a list of strings
    #fields = ('pub_date','question_text')

    #Listdisplay (ModelAdmin.list_display) expects either string or function as arguements 
    list_display = ('pub_date','question_text', decorateWasPublishedRecently )
    list_filter = ['pub_date']
    search_fields = ['question_text']
    inlines = [ChoiceInLine]

 


admin.site.site_header = 'Custom Django Header'
admin.site.site_tite = 'Custom Site Title'
admin.site.register(Question,QuestionAdmin)    

#admin.site.register(Choice)
