from django.shortcuts import render_to_response, render
from django.core.context_processors import csrf
from django.template import RequestContext
from django.http import HttpResponse
from django.template import Context, loader
import logging
import json

from demo.models import Project

logr = logging.getLogger(__name__)

# Create your views here.


def dashboard(request):
    args = {}
    projectList = Project.objects.all()
    args['project_list'] = projectList
    args.update(csrf(request))
    #return render_to_response('demo/dashboard/dashboard.html', {'project_list':projectList}  ,
    return render_to_response('demo/dashboard/dashboard.html', args  ,
                             context_instance=RequestContext(request))
    #return render_to_response('demo/dashboard/dashboard.html', {'project_list':projectList}, mimetype="application/xhtml+xml")

    #t = loader.get_template('demo/dashboard/dashboard.html')
    #c = Context({
    #    'project_list': projectList,
    #})
    #return HttpResponse(t.render(c))

def project(request, project_id):
    try:
        project_id = int(project_id)
    	project = Project.objects.filter(id=project_id)
    	args = {}
    	args['project_name'] =  project[0].project_name
        # dummy data for gauges 
    	args['clang_no'] =  10
    	args['lcov_no']  =  20
    	args['mcc_no']   =  30
    	args['cpd_no']   =  40
    	args['ct_no']    =  50

	#data = json.load(open('data.json'))
	data = [
        {
            "xScale":"ordinal",
            "comp":[],
            "main":[
                {
                    "className":".main.l1",
                    "data":[
                        { "y":15, "x":"2012-11-19T00:00:00" },
                        { "y":11, "x":"2012-11-20T00:00:00" },
                        { "y":8, "x":"2012-11-21T00:00:00" },
                        { "y":10, "x":"2012-11-22T00:00:00" },
                        { "y":1, "x":"2012-11-23T00:00:00" },
                        { "y":6, "x":"2012-11-24T00:00:00" },
                        { "y":8, "x":"2012-11-25T00:00:00" }
                    ]
                }
            ],
            "type":"line-dotted",
            "yScale":"linear"
        }
        ]

	print json.dumps(data)
	args['data'] =json.loads(json.dumps(data))
	args.update(csrf(request))
	return render_to_response('demo/project/project-dashboard.html', args,
                              context_instance=RequestContext(request))
    except ValueError:
        raise Http404()

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
