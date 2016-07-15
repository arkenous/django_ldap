from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return render_to_response(template_name='index.jinja', context={
        'distribution': 'arch',
    })
