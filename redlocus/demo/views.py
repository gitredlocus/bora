from django.shortcuts import render_to_response, render
from django.core.context_processors import csrf
from django.template import RequestContext

import logging

logr = logging.getLogger(__name__)

# Create your views here.

def dashboard(request):
    args = {}
    args.update(csrf(request))
    return render_to_response('demo/dashboard/dashboard.html', args,
                              context_instance=RequestContext(request))


def forms(request):
    args = {}
    args.update(csrf(request))
    return render_to_response('demo/forms/forms.html', args,
                              context_instance=RequestContext(request))


def charts(request):
    args = {}
    args.update(csrf(request))
    return render_to_response('demo/charts/charts.html', args,
                              context_instance=RequestContext(request))


def buttons(request):
    args = {}
    args.update(csrf(request))
    return render_to_response('demo/ui_lab/buttons.html', args,
                              context_instance=RequestContext(request))


def general(request):
    args = {}
    args.update(csrf(request))
    return render_to_response('demo/ui_lab/general.html', args,
                              context_instance=RequestContext(request))


def icons(request):
    args = {}
    args.update(csrf(request))
    return render_to_response('demo/ui_lab/icons.html', args,
                              context_instance=RequestContext(request))


def grid(request):
    args = {}
    args.update(csrf(request))
    return render_to_response('demo/ui_lab/grid.html', args,
                              context_instance=RequestContext(request))


def tables(request):
    args = {}
    args.update(csrf(request))
    return render_to_response('demo/ui_lab/tables.html', args,
                              context_instance=RequestContext(request))


def widgets(request):
    args = {}
    args.update(csrf(request))
    return render_to_response('demo/ui_lab/widgets.html', args,
                              context_instance=RequestContext(request))


def wizard(request):
    args = {}
    args.update(csrf(request))
    return render_to_response('demo/other/wizard.html', args,
                              context_instance=RequestContext(request))


def login(request):
    args = {}
    args.update(csrf(request))
    return render_to_response('demo/other/login.html', args,
                              context_instance=RequestContext(request))


def sign_up(request):
    args = {}
    args.update(csrf(request))
    return render_to_response('demo/other/sign_up.html', args,
                              context_instance=RequestContext(request))


def full_calendar(request):
    args = {}
    args.update(csrf(request))
    return render_to_response('demo/other/full_calendar.html', args,
                              context_instance=RequestContext(request))


def error404(request):
    args = {}
    args.update(csrf(request))
    return render_to_response('demo/other/error404.html', args,
                              context_instance=RequestContext(request))
