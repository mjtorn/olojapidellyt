# vim: tabstop=4 expandtab autoindent shiftwidth=4 fileencoding=utf-8

from django.db import models

class StoryManager(models.Manager):
    """Manage stories
    """

    def get_visible(self):
        """Visible stories
        """

        return self.select_related('user').filter(visible=True)

    def get_recent(self):
        """Recent stories
        """

        recent = self.get_visible().order_by('-posted_at')
        recent = recent[:5]

        return recent

    def get_top_moods(self):
        """Top moods
        """

        top_moods = self.get_visible().order_by('-posted_at', '-mood')
        top_moods = top_moods[:5]

        return top_moods

    def get_random_story(self):
        """Returns None if nothing found
        """

        random_story = self.get_visible().order_by('?')
        try:
            random_story = random_story[0]
        except IndexError:
            random_story = None

        return random_story

# EOF

