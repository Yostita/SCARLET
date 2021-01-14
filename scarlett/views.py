from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import json
from django.views.decorators.csrf import csrf_exempt
from manage import get_scarlet_renponse


@csrf_exempt
def get_response(request):
    response = {'status': None}

    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        message = data['message']
        chat_response = get_scarlet_renponse(message)
        response['message'] = {'text': chat_response}
        response['status'] = 'ok'

    else:
        response['error'] = 'no post data found'

    return HttpResponse(
        json.dumps(response),
        content_type="application/json"
    )


@login_required
def home(request):
    return render(request, 'scarlett/index.html', {'title': 'Scarlett'})


def dash(request):
    return render(request, 'scarlett/404.html', {'title': '404'})
