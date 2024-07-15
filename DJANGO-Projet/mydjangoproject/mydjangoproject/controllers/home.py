from django.shortcuts import render,redirect
from mydjangoproject.models.personne import Personne
from django.views.decorators.http import require_http_methods


@require_http_methods(['POST'])
def home(request):
    per = Personne()
    return render(request,'index.html', {'personne':per})