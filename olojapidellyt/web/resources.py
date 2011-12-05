# vim: tabstop=4 expandtab autoindent shiftwidth=4 fileencoding=utf-8

from django.shortcuts import get_object_or_404

from olojapidellyt.web import models

from dagny import Resource, action

class Story(Resource):
    """Story resource
    """

    @action
    def index(self):
        self.stories = models.Story.objects.get_visible().order_by('-posted_at')

    @action
    def show(self):
        slug = self.params.get('slug', None)
        self.story = get_object_or_404(models.Story, visible=True, slug=slug)

# EOF

