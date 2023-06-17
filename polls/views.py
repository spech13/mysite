from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from polls.models import Question, Choice
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {"latest_question_list":latest_question_list,}
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, "polls/detail.html", {"question": question})

def results(requests, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(requests, "polls/results.html", {"question":question})

def vote(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    try:
        selected_choice = question.choice_set.get(id=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {"question":question, "error_message":"You didn't select a choice."})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

