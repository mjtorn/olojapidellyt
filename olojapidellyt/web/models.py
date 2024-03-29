# vim: tabstop=4 expandtab autoindent shiftwidth=4 fileencoding=utf-8

from django.contrib.auth import models as auth_models

from annoying.decorators import signals

from django.db import models

from django.template import defaultfilters

from olojapidellyt.web import managers

from django_facebook import models as facebook_models

# Create your models here.

class UserProfile(facebook_models.FacebookProfileModel, models.Model):
    """Basic user profile stuff
    """

    user = models.OneToOneField(auth_models.User)

    description = models.TextField(help_text='Kuvaus')

    def __unicode__(self):
        return u'%s' % self.user

    def remove_fb_profile(self):
        """Facebook wants us to be able to do this :(
        """

        for f in facebook_models.FacebookProfileModel._meta.fields:
            setattr(self, f.name, None)

        self.raw_data = ''
        self.save()

        self.user.is_active = False
        self.user.save()


@signals.post_save(sender=auth_models.User)
def create_profile(instance, **kwargs):
    if kwargs['created']:
        profiel = UserProfile.objects.create(user=instance)


class Story(models.Model):
    """Story model
    """

    user = models.ForeignKey(auth_models.User, null=True, default=None)
    username = models.CharField(help_text='Vapaaehtoinen nimimerkki', max_length=30, null=True, blank=True, default=None)

    posted_at = models.DateTimeField(auto_now_add=True, db_index=True)

    heading = models.CharField(help_text='Vapaaehtoinen otsikko', max_length=255, blank=True)
    content = models.TextField(help_text='Olo')

    slug = models.SlugField()

    visible = models.BooleanField(default=True, db_index=True)

    mood = models.IntegerField(help_text='Fiilis')

    objects = managers.StoryManager()

    def __unicode__(self):
        return u'%s' % self.heading

    def get_heading(self):
        """Use the first sentence
        """

        return self.content.split('.', 1)[0]

    def get_description(self):
        """Get the first three sentences
        """

        return '.'.join(self.content.split('.', 4)[:4])

    def save(self, *args, **kwargs):
        """Slugifying save
        """

        if not self.heading:
            self.heading = self.get_heading()

        if not self.slug:
            i = 0
            orig_slug = defaultfilters.slugify(self.heading)
            use_slug = orig_slug
            good = False
            while not good:
                good = self.__class__.objects.filter(slug=use_slug).count() == 0
                if good:
                    self.slug = use_slug
                else:
                    i += 1

                    use_slug = '%s-%d' % (orig_slug, i)

        return super(Story, self).save(*args, **kwargs)

# EOF

