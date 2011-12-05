# vim: tabstop=4 expandtab autoindent shiftwidth=4 fileencoding=utf-8

from django.shortcuts import render_to_response

from django.template import RequestContext

from olojapidellyt.web import models

# Create your views here.

def index(request):
    """Probably the only view in town
    """

    recent = models.Story.objects.get_visible()
    recent = recent.order_by('-posted_at')
    recent = recent[:5]

    req_ctx = RequestContext(request, locals())

    return render_to_response('index.html', req_ctx)

# EOF

