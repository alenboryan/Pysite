import re
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login as auth_login, logout, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User

from .models import Choice, PyUser, Info, Question, Studying, Pysyntax, DjangoInfo , Pyintro
from .forms import InfoForm
from django.urls import reverse

def index(request):
    return render(request, 'info/index.html')

def about(request):
    return render(request, 'info/about.html')

def login(request):
    if request.method == 'GET':
        return render(request, "info/login.html")
    else:
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        if user:
            auth_login(request, user)
            return HttpResponseRedirect("/info/")
        else:
            return render(request, "info/login.html", context={"error": "Incorrect username or password"})

def register(request):
    if request.method == 'GET':
        return render(request, "info/register.html")
    else:
        username = request.POST["username"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        password = request.POST['password']
        
        if firstname == username or lastname == username:
            return render(request, "info/error.html", context={"error": "First name or last name cannot be the same as username"})
        
        if len(password) <= 8 or not re.search("[a-z]", password) or not re.search("[A-Z]", password) \
                or not re.search("[0-9]", password) or not re.search("[_@$]", password):
            return render(request, "info/error.html", context={"error": "Password must be at least 8 characters long and contain at least one lowercase letter, one uppercase letter, one digit, and one of the following symbols: _@$"})
        
        user = User.objects.create_user(username=username, password=password)
        user.first_name = firstname
        user.last_name = lastname
        user.save()
        PyUser(user=user).save()
        return redirect("/info/login")

def log_out(request):
    logout(request)
    return HttpResponseRedirect("/info/login")

def python_introduction(request):
    contents = Pyintro.objects.all()
    return render(request, "info/intro.html",{'contents': contents})

def python_syntax(request):
    contents = Pysyntax.objects.all()
    return render(request, 'info/syntax.html', {'contents': contents})

def error(request):
    return render(request, "info/error.html")

def create(request):
    if request.method == 'POST':
        form = InfoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/info/')
    else:
        form = InfoForm()
    
    return render(request, 'info/create.html', {'form': form})

def add_info(request):
    info = Info.objects.all()
    return render(request, 'info/infousers.html', {"info": info})

def django_info(request):
    contents = DjangoInfo.objects.all()
    return render(request, 'info/django.html', {'contents': contents})


def flask_info(request):
    return render(request, 'info/flask.html')

def pandas_info(request):
    return render(request, 'info/pandas.html')

def numpy_info(request):
    return render(request, 'info/numpy.html')


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "info/detail.html", {"question": question})


def results(request):
    # Retrieve all questions
    questions = Question.objects.all()
    
    # Check if there are no questions available
    if not questions:
        return render(
            request,
            "info/detail.html",
            {
                "error_message": "No questions available.",
            },
        )

    return render(request, "info/results.html", {"questions": questions})

def vote(request):
    questions = Question.objects.all()

    if request.method == 'POST':
        try:
            question_id = request.POST["question_id"]
            question = get_object_or_404(questions, pk=question_id)
            selected_choice = question.choice_set.get(pk=request.POST["choice"])
        except (KeyError, Choice.DoesNotExist, Question.DoesNotExist):
            return render(
                request,
                "info/detail.html",
                {
                    "questions": questions,
                    "error_message": "You didn't select a choice.",
                },
            )
        else:
            selected_choice.votes += 1
            selected_choice.save()
            return HttpResponseRedirect(reverse("info:results"))

    return render(request, "info/detail.html", {"questions": questions})

def studying(request):
    content = Studying.objects.all()
    return render(request, 'info/studying.html',{"content":content})
        