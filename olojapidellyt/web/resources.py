# vim: tabstop=4 expandtab autoindent shiftwidth=4 fileencoding=utf-8

from django.core.urlresolvers import reverse

from django.contrib import messages

from django.db.models import F

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
        if self.request.user.id:
            self.form.initial['username'] = self.request.user.username
        self.action = reverse('Story#create')

    @action
    def create(self):
        data = self.request.POST.copy() or None
        self.form = forms.Story(data)
        if self.form.is_bound:
            if self.form.is_valid():
                self.story = self.form.save(commit=False)
                if self.request.user.id:
                    self.story.user = self.request.user
                self.story.save()

                messages.success(self.request, 'Olo lisättiin onnistuneesti!')

                return redirect('Story#show', self.story.slug)

        return self.new.render()


class UserProfile(Resource):
    """UserProfile resource
    """

    @action
    def show(self):
        username = self.params.get('username', None)

        self.is_you = username == self.request.user.username

        self.profile = get_object_or_404(models.UserProfile, user__username=username)

        self.stories = self.profile.user.story_set.filter(visible=True)
        if not self.is_you:
            self.stories = self.stories.filter(username=F('user__username'))
        self.stories = self.stories.order_by('-posted_at')

    @action
    def edit(self):
        username = self.params.get('username', None)
        if username != self.request.user.username:
            if not self.request.user.id:
                messages.error(self.request, 'Kirjaudupa ensin sisään')
                return redirect(reverse('index'))
            messages.error(self.request, 'Äläpä yritä hakkeroida toisten tiliä')
            return redirect('UserProfile#show', self.request.user.username)

        self.form = forms.UserProfile(initial={
            'description': self.request.user.get_profile().description,
        })
        self.action = reverse('UserProfile#update', args=(self.request.user.username,))

    @action
    def update(self):
        username = self.params.get('username', None)
        if username != self.request.user.username:
            if not self.request.user.id:
                messages.error(self.request, 'Kirjaudupa ensin sisään')
                return redirect(reverse('index'))
            messages.error(self.request, 'Äläpä yritä hakkeroida toisten tiliä')
            return redirect('UserProfile#show', self.request.user.username)

        data = self.request.POST.copy() or None

        self.form = forms.UserProfile(data, instance=self.request.user.get_profile())
        self.action = reverse('UserProfile#update', args=(self.request.user.username,))

        if self.form.is_bound:
            if self.form.is_valid():
                self.form.save()
                return redirect('UserProfile#show', self.request.user.username)

# EOF

