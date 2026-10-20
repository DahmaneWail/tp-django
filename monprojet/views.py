
from django.http import HttpResponse

def accueil(request):
  return HttpResponse("<h1>Bienvenue sur ma premi re page Django !</h1>")
                                               