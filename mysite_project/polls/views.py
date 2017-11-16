# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Question,Choice
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.shortcuts import render,get_object_or_404,get_list_or_404
from django.http import Http404
from django.urls import reverse
from django.db.models import F
from django.views import generic
from django.utils import timezone

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = ', '.join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))

# def index(request,request_text=None):
#     latest_question_list = Question.objects.order_by('-pub_date')[:10]
#     # template = loader.get_template('polls/index.html')
#     # output = '</p><p>'.join([q.question_text for q in latest_question_list])
#     # output = "<h1><p>{}</p></h1>".format(output)
#     context = {
#         'latest_question_list': latest_question_list,
#         'request_text':request_text,
#     }
#     return render(request,'polls/index.html',context)

# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk = question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question id {} does not exist".format(question_id))
#     return render(request , 'polls/detail.html' , {'question':question})

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     # choice = get_object_or_404(Choice, pk=question_id)
#     return render(request , 'polls/detail.html' , {'question':question})


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request , 'polls/results.html' , {
#         'question':question,
#     })


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request , 'polls/results.html' , {
#         'question':question,
#     })

def vote(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    # selected_choice = question.choice_set.get(pk=request.POST['choice3'])
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice2'])
    except (KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html',{
                'question':question,
                'error_message':u"没有POST所需参数",
            })

    else:
        # selected_choice.votes += 1
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        # """ 返回最近时间的五个问题 """
        # return Question.objects.order_by('-pub_date')[:5]

        """返回最近发布的五个投票（不包括那些被设置为在将来发布的）"""
        return Question.objects.filter(
            pub_date__lte = timezone.now()
        ).order_by('-pub_date')[:10]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    context_object_name = 'question'
    template_name = 'polls/results.html'