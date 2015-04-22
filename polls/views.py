from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.views import generic

from polls.models import Question, Choice

#clases

class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		#retorna a la publicacion de las preguntas
		return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'
		

def vote(request, question_id):
	p = get_object_or_404(Question, pk = question_id)
	try :
		selected_choice = p.choice_set.get(pk = request.POST['choice'])
	except (KeyError, Choice.DoesNotExist) :
		return render(request, 'polls/detail.html',{
				'question':p,
				'error_message':"No ha seleccionado ninguna respuesta.",
			})
	else :
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results', args = (p.id,)))



#Escribe vistas que realmente hacen algo 
#Write views that actually do something