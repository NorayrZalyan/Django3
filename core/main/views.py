from django.shortcuts import render , redirect
from django.views import View   
from .models import *
from django.contrib.auth.models import User


from django.contrib.auth import authenticate, login, logout


class index(View):
    template_name = 'index.html'
    def get(self , request):
        Header_list = H_Header.objects.all()
        about_company_list = H_about_company.objects.all()
        Work_list = Work.objects.all()
        About_list = About.objects.all()
        A_link_list = A_link.objects.all()
        contact_list = contact.objects.all()
        return render(request , self.template_name , 
                       {'Header_list':Header_list,
                       'about_company_list':about_company_list,
                       'Work_list':Work_list,
                       'About_list':About_list,
                       'A_link_list':A_link_list,
                       'contact_list':contact_list
         })







def user_login(request):
    er = False
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request , username=username , password=password)
        if user is not None:
            login(request , user)
            return redirect('index')
        else:
            er = True
            return render(request , 'login.html' , {'error': 'пользователя не сушествует',
                                                     'er':er})
    else:
        return render(request , 'login.html')




def user_logout(request):
    logout(request)
    return redirect('index')







def user_register(request):
    er = False
    errors = []
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if User.objects.filter(username=username).exists():
            err = 'Пользователь с таким именем уже существует.'
            errors.append(err)
            er = True
        if User.objects.filter(email=email).exists():
            err = 'Пользователь с таким именем уже существует.'
            errors.append(err)
            er = True
        if username == password:
            err = 'Пароль не должен совпадать с именем пользователя.'
            errors.append(err)
            er = True
        if len(password) < 8:
            err = 'Пароль должен содержать не менее 8 символов.'
            errors.append(err)
            er = True
        if password2 != password:
            err = 'Пароль не совподоют'
            errors.append(err)
            er = True

        if er:
            return render(request , 'register.html', {'errors':errors , 'er':er})

        user = User.objects.create_user(username=username, email=email,  password=password)
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
    return render(request, 'register.html')








