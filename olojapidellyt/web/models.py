# vim: tabstop=4 expandtab autoindent shiftwidth=4 fileencoding=utf-8

from django.contrib.auth import models as auth_models

from annoying.decorators import signals

from django.db import models

from django.template import defaultfilters

from olojapidellyt.web import managers

# Create your models here.

class UserProfile(models.Model):
    """Basic user profile stuff
    """

    user = models.OneToOneField(auth_models.User)

    description = models.TextField()

    def __unicode__(self):
        return u'%s' % self.user

@signals.post_save(sender=auth_models.User)
def create_profile(instance, **kwargs):
    if kwargs['created']:
        profiel = UserProfile.objects.create(user=instance)


class Story(models.Model):
    """Story model
    """

    user = models.ForeignKey(auth_models.User, null=True, default=None)

    posted_at = models.DateTimeField(auto_now_add=True, db_index=True)

    heading = models.CharField(help_text='Otsikko', max_length=255)
    content = models.TextField(help_text='Tarina')

    slug = models.SlugField()

    visible = models.BooleanField(default=True, db_index=True)

    objects = managers.StoryManager()

    def save(self, *args, **kwargs):
        """Slugifying save
        """

        if not self.slug:
            i = 0
            orig_slug = defaultfilters.slugify(self.heading)
            use_slug = orig_slug
            good = False
            while not good:
                good = self.__class__.objects.filter(slug=use_slug).count() == 0
                if good:
                    self.slug = use_slug
                    return super(Story, self).save(*args, **kwargs)
                else:
                    i += 1

                use_slug = '%s-%d' % (orig_slug, i)

# EOF

