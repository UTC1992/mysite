from django.contrib import admin
from polls.models import Question, Choice

#TabularInline o StackedInline
class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

#modelo de interfaz para la administracion 
class QuestionAdmin(admin.ModelAdmin):
	#fields = ['pub_date','question_text']
	fieldsets = [
		(None, 				  {'fields': ['question_text']}),
		('Datos Informacion', {'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	inlines = [ChoiceInline]
	#para mostrar campos individuales
	list_display = ('question_text', 'pub_date','was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['question_text']

# Register your models here.
#el modelo se lo puede pasar como un segundo argumento 
admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)


#Personalizar la lista de cambios del administrador