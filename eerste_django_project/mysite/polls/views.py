from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choice
import datetime 
from django.utils import timezone
from django.template import loader
from django.urls import reverse
from django.views import generic

# Create your views here.

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name="latest_question_list"

    def get_queryset(self) -> QuerySet[Any]:
        return Question.objects.filter(pub_date__lte = timezone.now()).order_by("-pub_date")

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        question = Question.objects.filter(pub_date__lte=timezone.now())
        return question


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"



def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")
    template = "polls/index.html"
    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request, template, context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question,
    }
    template = "polls/detail.html"
    return render(request, template, context)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        "question" : question,
    }
    template = "polls/results.html"
    return render(request, context=context, template_name=template)


def vote(request, question_id): 
    question = get_object_or_404(Question, pk = question_id)
    # print(question.choice_set.all())
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except(KeyError, Choice.DoesNotExist) as e:
        return redirect("polls:detail", question_id)
    # Choice.objects.get(pk = request.POST["choice"])
    print(selected_choice)

    selected_choice.votes += 1
    selected_choice.save()

    return HttpResponseRedirect(reverse('polls:results', args=(question_id, )))


def test_db(request):
    print("--- Dit is een test ---")

    all_questions = Question.objects.all()

    print(all_questions)

    q = Question(question_text ="Question 3e les !", pub_date=datetime.datetime.now())

    # q.save()

    # print(f"Question aangemaakt met id: {q.id}, text: {q.question_text}, datum: {q.pub_date}")

    # all_questions = Question.objects.all()

    # for question in all_questions:
    #     if question.was_published_recently():
    #         print(question.question_text, question.was_published_recently())

    # q_1 = Question.objects.get(id=1)
    # print(f"We hebben question met id {q_1.id} opgehaald")

    # q_1 = Question.objects.filter(id=1)
    # print(f"We hebben question met id {q_1[0].id} opgehaald")

    qs = Question.objects.filter(question_text__startswith = "Question")
    print(qs)

    current_year = timezone.now().year
    current_day = timezone.now().day
    qs_2 = Question.objects.filter(pub_date__year=current_year)
    print(qs_2)
    qs_3 = Question.objects.filter(pub_date__day=current_day)
    print(qs_3)

    previous_year = (timezone.now()-datetime.timedelta(weeks=52)).year
    qs_4 = Question.objects.filter(pub_date__year=previous_year)
    print(qs_4)

    q_5 = Question.objects.get(pk=1)
    choices = q_5.choice_set.all()
    # print(choices)

    q_5.choice_set.create(choice_text="Not much", votes =0)
    q_5.choice_set.create(choice_text="The Sky")
    
    c = Choice(question = q_5, choice_text="Just Hacking", votes=0)
    # c.save()

    print(q_5.choice_set.count())

    previous_year = (timezone.now()-datetime.timedelta(weeks=52)).year
    choices_from_questions_previous_year = Choice.objects.filter(question__pub_date__year=previous_year)
    print(choices_from_questions_previous_year)
    
    choices_question_with_id_1 = Choice.objects.filter(question__id=1)
    print(choices_question_with_id_1)

    c_1 = q_5.choice_set.filter(choice_text__startswith="Just")
    c_1.delete()

    return HttpResponse("Check the print on your server")

