# vim: tabstop=4 expandtab autoindent shiftwidth=4 fileencoding=utf-8

from olojapidellyt.web import models

from django import forms

MOOD_CHOICES = (
    (-1, -1),
    (0, 0),
    (1, 1),
)

from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe

class OtherRadioFieldRenderer(forms.widgets.RadioFieldRenderer):
    def render(self):
        return mark_safe(u'<div class="radio">\n%s\n<div>' % u'\n'.join([u'%s %s' % (force_unicode(w.tag()), force_unicode(w.choice_label)) for w in self]))

class Story(forms.ModelForm):
    """Story form
    """

    class Meta:
        model = models.Story
        exclude = ('user', 'posted_at', 'slug', 'visible')

    def __init__(self, *args, **kwargs):
        self.base_fields['mood'].widget = forms.widgets.RadioSelect(choices=MOOD_CHOICES, renderer=OtherRadioFieldRenderer)

        return super(Story, self).__init__(*args, **kwargs)


class UserProfile(forms.ModelForm):
    """Story form
    """

    class Meta:
        model = models.UserProfile
        fields = ('description',)

# EOF

