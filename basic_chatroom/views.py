from django.http import HttpResponse
from django.shortcuts import render
import json

from django.template.context_processors import csrf


def challenge_1(request):
    data = []
    with open('data.json') as f:
        for line in f:
            data.append(json.loads(line))


    args= {}
    args.update(csrf(request))

    args['data'] = list(data)
    args['count'] = len(data)


    return render(request, 'challenge_1.html', args)



def pdf_view(request):
    with open('opnbxai.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(),content_type='application/pdf')
        response['Content-Disposition'] = 'filename=opnbxai.pdf'
        return response
