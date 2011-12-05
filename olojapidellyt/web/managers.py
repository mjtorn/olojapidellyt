# vim: tabstop=4 expandtab autoindent shiftwidth=4 fileencoding=utf-8

from django.db import models

class StoryManager(models.Manager):
    """Manage stories
    """

    def get_visible(self):
        """Visible stories
        """

        return self.select_related('user').filter(visible=True)

# EOF

