# vim: tabstop=4 expandtab autoindent shiftwidth=4 fileencoding=utf-8

from django.core.urlresolvers import reverse

from django.shortcuts import render_to_response

from django.template import RequestContext

from olojapidellyt.web import forms, models

# Create your views here.

def index(request):
    """Probably the only view in town
    """

    visible_stories = models.Story.objects.get_visible()

    recent = visible_stories.order_by('-posted_at')
    recent = recent[:5]

    random_story = visible_stories.order_by('?')
    try:
        random_story = random_story[0]
    except IndexError:
        random_story = None

    form = forms.Story(initial={
        'mood': 0,
    })
    if request.user.id:
        form.initial['username'] = request.user.username
    action = reverse('Story#create')

    req_ctx = RequestContext(request, locals())

    return render_to_response('index.html', req_ctx)

# EOF

