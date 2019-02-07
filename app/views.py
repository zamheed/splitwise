from django.shortcuts import render
from .models import Expenditure
from .models import Register


def welcome(request):
    email = request.POST.get('email')
    pwd = request.POST.get('pwd')
    if Register.objects.filter(email=email, psw=pwd):
        request.session['login'] = email
        user = request.session['login']
        data = Register.objects.all()
        return render(request, 'welcome.html', {'data': data, 'user': user})
    else:
        return render(request, "login.html", {"mess": "LOGIN ERROR"})


def signup(request):
    cont = request.POST.get('contact')
    name = request.POST.get('name')
    email = request.POST.get('email')
    pwd = request.POST.get('password')
    Register(cont=cont, name=name, email=email, psw=pwd).save()
    return render(request, "login.html")


def add(request):
    expense = request.POST.get('expense')
    cost = request.POST.get('cost')
    date = request.POST.get('date')
    mails = request.POST.getlist('mails')
    val = int(cost)/int(len(mails))
    for x in mails:
        Expenditure(email_id=x, date=date, expense=expense, cost=val).save()
    return render(request, "welcome.html", {"msg": "Expense Added", 'data': date})


def get_data(request):
    frdt = request.POST.get('from')
    to = request.POST.get('to')
    if frdt == '' or to == '':
        return render(request, "welcome.html", {"error": "Select Dates"})
    else:
        ex = Expenditure.objects.filter(date__range=[frdt, to])
        return render(request, "welcome.html", {"ex": ex})


def get_my_data(request):
    frdt = request.POST.get('start')
    to = request.POST.get('end')
    if frdt == '' or to == '':
        return render(request, "welcome.html", {"error": "Select Dates"})
    else:
        user = request.session['login']
        ex = Expenditure.objects.filter(date__range=[frdt, to], email_id=user)
        return render(request, "welcome.html", {"my_exp": ex,'user':user})

