import random

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from mydj1.models import Testm, UserModel


def index (request):
    # n = Testm()
    # n.log = 'Dima'+str(random.randint(1,10))
    # n.pas = random.randint(1, 100)
    # n.save()
    # s = Testm.objects.all()
    # arlog = []
    # arpas = []
    # arall = []
    # for i in s: arlog.append(i.log)
    # for i in s: arpas.append(i.pas)
    # d = {}
    #
    # for i in s:
    #     d[i.log] = i.pas

    return render(request, 'index.html',  {'hello':'Здравствуйте, Гость'})

def new (request):
    return render(request, 'New.html', {'hi':'Mailinovskiy'})

def reverse (request):
    return render(request, 'Revers.html')

@csrf_exempt
def reg(request):    #Регистрация пользователя
    if request.method == 'POST':
        # обработка POST запроса
        l = request.POST['login']
        p = request.POST['pas']
        e = request.POST['email']
        n = UserModel()
        arrlog = []
        arrpas = []
        for i in UserModel.objects.all(): #прохождение по всме записям модели UserModel
            arrlog.append(i.log)  #Добавление логинов в список
            arrpas.append(i.pas)  #Добавление паролей в список
        if l in arrlog:    #Если такрй логин есть, то ошибка!
            return render(request, 'Error.html')
        n.log = l  #Если такого логина нет, то добавляем его в модель
        n.pas = p
        n.email = e
        n.save()
        #return render(request, 'New.html') # и отправляем на новую страницу
        return redirect(f'/New?hello=Helloy, {l}')   #передаем в адресную сторку
    return render(request, 'Autorisation.html')

def page_auth(request):
    return render(request, 'Autorisation.html')

@csrf_exempt
def auth(request):
    if request.method == 'POST':
        l = request.POST['login']
        p = request.POST['pas']
        diclog = dict()

        for i in UserModel.objects.all():
            diclog[i.log] = i.pas

        if l in diclog.keys() and p == diclog[l]:
            return redirect(f'/New?hello=Helloy, {l}')

        else:
            return render(request, 'Error_aut.html', {'x':'Ошибка!'})

def page_reg(request):
    return render(request, 'Registration.html')

def autor(request):
    l = request.POST['login']
    p = request.POST['pas']
    n = Testm()
    n.log = l
    n.pas = p
    n.save()
    return render(request, 'Autorisation.html', {'yes':'Авторизация прошла успешно'})
def rev (request):
    t = request.GET['usertext']
    arr = []
    tex = list(t)
    arr.extend(tex)
    arr.reverse()
    text = ''
    for i in arr: text += i
    return render(request, 'Revers2.html',{"data":text})
# Create your views here.
