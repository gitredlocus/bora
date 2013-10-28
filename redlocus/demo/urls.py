from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^dashboard/', 'demo.views.dashboard'),
    url(r'^forms/', 'demo.views.forms'),
    url(r'^charts/', 'demo.views.charts'),
    url(r'^project/', 'demo.views.project'),
    # ui_lab
    url(r'^ui_lab/buttons', 'demo.views.buttons'),
    url(r'^ui_lab/general', 'demo.views.general'),
    url(r'^ui_lab/icons', 'demo.views.icons'),
    url(r'^ui_lab/grid', 'demo.views.grid'),
    url(r'^ui_lab/tables', 'demo.views.tables'),
    url(r'^ui_lab/widgets', 'demo.views.widgets'),
    # other
    url(r'^other/wizard', 'demo.views.wizard'),
    url(r'^other/login', 'demo.views.login'),
    url(r'^other/sign_up', 'demo.views.sign_up'),
    url(r'^other/full_calendar', 'demo.views.full_calendar'),
    url(r'^other/error404', 'demo.views.error404'),
)
