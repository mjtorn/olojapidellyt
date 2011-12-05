# vim: tabstop=4 expandtab autoindent shiftwidth=4 fileencoding=utf-8

from django.core.urlresolvers import reverse

from django.shortcuts import get_object_or_404, redirect

from olojapidellyt.web import forms, models

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

        self.title = self.story.heading
        self.meta_description = self.story.get_description()

    @action
    def new(self):
        self.form = forms.Story(initial={
            'mood': 0,
        })
        self.action = reverse('Story#create')

    @action
    def create(self):
        data = self.request.POST.copy() or None
        self.form = forms.Story(data)
        if self.form.is_bound:
            if self.form.is_valid():
                self.story = self.form.save()

                return redirect('Story#show', self.story.slug)

        return self.new.render()


class UserProfile(Resource):
    """UserProfile resource
    """

    @action
    def show(self):
        username = self.params.get('username', None)
        self.profile = get_object_or_404(models.UserProfile, user__username=username)

        self.stories = self.profile.user.story_set.filter(visible=True).order_by('-posted_at')

# EOF

