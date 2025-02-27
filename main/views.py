from django.utils.translation import gettext as _
from django.shortcuts import render

def home(request):
    context = {'message': _("Witamy w naszym sklepie!")}
    return render(request, 'home.html', context)
