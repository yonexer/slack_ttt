from django.views.decorators.http import require_POST
from django.http.response import HttpResponse
from game.form.ttt_form import TTTForm

@require_POST
def play(request):
    ttt_form = TTTForm(request.POST)
    if ttt_form.is_valid():
        result = ttt_form.process()
        return HttpResponse(result)
    else:
        return HttpResponse('Invalid')
