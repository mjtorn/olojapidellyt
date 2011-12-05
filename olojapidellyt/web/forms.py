# vim: tabstop=4 expandtab autoindent shiftwidth=4 fileencoding=utf-8

from olojapidellyt.web import models

from django import forms

class Story(forms.ModelForm):
    """Story form
    """

    class Meta:
        model = models.Story
        exclude = ('user', 'posted_at', 'slug', 'visible')

# EOF

