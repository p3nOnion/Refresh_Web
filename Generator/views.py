import random

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render( request,'generator/home.html' )


def passwd(request):
    thepassword = ''
    characters = list( 'abcdefghijklmnopqrstuvxyz' )
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIKLMNOPQRSTUVXYZ'))
    if request.GET.get('number'):
        characters.extend(list('1234567890'))
    if request.GET.get('special'):
        characters.extend(list(" #$%&'()*+,-./:;<=>?@[\]^_`{|}~"))
    lenght = int(request.GET.get('lenght',12))
    for i in range( lenght ):
        thepassword += random.choice( characters )
    return render( request,'generator/passwd.html',{'password': thepassword} )


def account(request):
    return render( request,'generator/account.html' )
def about(request):
    return render(request, 'generator/about.html')
