from django.conf.urls import patterns, include, url
from polls import views

urlpatterns = patterns ('',
		# ejem: /polls/
		url(r'^$', views.IndexView.as_view(), name = 'index'),
		# ejem: /polls/5/
		url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
		# ejem: /polls/5/results/
		url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
		# ejem: /polls/5/vote/
    	url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
	)