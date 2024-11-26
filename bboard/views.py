from django.http import HttpResponse
from django.shortcuts import render

from .models import Bb

def index(request):
    # template = loader.get_template('bboard/index.html')
    # bbs = Bb.objects.order_by('-published')
    bbs = Bb.objects.all()
    return render(request, 'bboard/index.html', {'bbs': bbs})