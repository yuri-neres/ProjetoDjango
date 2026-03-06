from django.http import HttpResponse
from Produto.models import Produto

def home(request):
    return HttpResponse("Ola Django!")