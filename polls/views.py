from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from .models import Question
from django.shortcuts import get_object_or_404, render
from django.utils.html import escape
from django.urls import reverse
from django.views import generic
from django.utils import timezone
#from django.utils import datetime

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    #This is the variable name which will be used to load the value (the query set obtained)
    #Which means in python , it is possible to run another code ??
    context_object_name = 'latest_question_list'
    #Query set (Iterable)
    #Using filters on queryset
    #https://docs.djangoproject.com/en/2.1/topics/db/queries/#retrieving-specific-objects-with-filters
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')
        #return Question.objects.filter(pub_date__lte=datetime.date.today())
        #.order_by('pub_date')

class DetailsView(generic.DetailView):
    model = Question
    template_name  = 'polls/question_detail.html'

'''
# For future reference , in case you wan to know the basics related to 'Function views' instead of 'Class Views'
def details(request,question_id):
    #return HttpResponse("(Under Implementation)Hello thanks for asking about a question ,this is the question id you asked for %s" % question_id)
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    #print("Moving after exception")
    #context is the one which connects 'question' in view to the 'question' in template
    context = {'question' : question}
    return render(request,'polls/question_detail.html', context)
'''
#'''
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/result.html'
#'''
#
'''
def results(request,question_id):
    question=get_object_or_404(Question , pk=question_id)
    context = { 'question' : question }
    return render(request , 'polls/result.html', context)
#
'''    

def vote(request,question_id):
    #return HttpResponse("(Under implementation ) You are looking at the no of votes for the question no :  %s" % question_id)
    question=get_object_or_404(Question , pk=question_id)
    print(request.POST)
    
    #Now we got a reference to the choice object
    choice = question.choice_set.get(pk=request.POST.get('choice'))
    choice.votes = choice.votes + 1 
    choice.save()

    #Now comes the redirection logic
    return HttpResponseRedirect(reverse('results', args=[question.id]))
