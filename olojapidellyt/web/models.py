# vim: tabstop=4 expandtab autoindent shiftwidth=4 fileencoding=utf-8

from django.contrib.auth import models as auth_models

from annoying.decorators import signals

from django.db import models

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

# EOF

