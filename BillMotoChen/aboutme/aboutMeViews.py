from datetime import datetime
import logging

from django.shortcuts import *
from django.http import HttpResponse
from aboutme.classes import player
from aboutme.models import Career

# Create your views here.

def health_check(request):
    # logging.info('AboutMe Health Check is Accessed at :' + str(datetime.now()))
    return HttpResponse("About me is working: " + str(datetime.now()))

def self_introduction(request):
    return render(request, 'aboutme/index.html')

def hobbies(request):
    return render(request, 'aboutme/hobbies.html')

def test(request, id):
    me = player.player()
    kayu = player.player('Kayu', 27)
    couple = [me, kayu]
    all_event = Career.objects.all()
    career = get_object_or_404(Career, pk=id)
    return render(request, "aboutme/test.html",
                  {"couple": couple, "event": career,
                   "events": all_event,
                   })
