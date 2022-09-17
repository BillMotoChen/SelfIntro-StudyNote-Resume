from datetime import datetime
import logging

from django.shortcuts import *
from django.http import HttpResponse
from aboutme.classes import player
from aboutme.models import Career, Pieces
from aboutme.etc import constant

# Create your views here.

def health_check(request):
    # logging.info('AboutMe Health Check is Accessed at :' + str(datetime.now()))
    return HttpResponse("About me is working: " + str(datetime.now()))

def self_introduction(request):
    return render(request, 'aboutme/index.html')

def hobbies(request):
    return render(request, 'aboutme/hobbies/hobbies.html')

def pieces_search(request):
    composer = request.GET.get('composer')
    tonality = request.GET.get('tonality')
    status = request.GET.get('status')
    sort = request.GET.get('sort')

    pieces_list = Pieces.objects.all()

    if composer != '':
        pieces_list = pieces_list.filter(composer=composer)
    if tonality != '':
        pieces_list = pieces_list.filter(tonality=constant.TONALITY[int(tonality)])
    if status != '':
        pieces_list = pieces_list.filter(status=status)

    # TODO: to be tested
    if sort == 0:
        pieces_list = pieces_list.order_by('difficulty')
    elif sort == 1:
        pieces_list = pieces_list.order_by('difficulty')[::-1]
    elif sort == 2:
        pieces_list = pieces_list.order_by('status')
    elif sort == 3:
        pieces_list = pieces_list.order_by('tonality')

    return render(request, 'aboutme/hobbies/pieces_search.html', {"pieces": pieces_list})

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
