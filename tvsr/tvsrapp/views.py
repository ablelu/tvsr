from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Movie


def index(request):
    movies = Movie.objects
    return render_to_response('index.html', {'Movies': movies},
                            context_instance=RequestContext(request))
        

def show(request, subject_id):
    movie = Movie.objects(subject_id = subject_id)[0]
    return render_to_response('show.html', {'movie': movie},
                            context_instance=RequestContext(request))


def boot(request):
    movie = Movie.objects(subject_id = '6386345')[0]
    return render_to_response('boot.html', {'movie': movie},
                            context_instance=RequestContext(request))


# Create your views here.
