# vim: tabstop=4 expandtab autoindent shiftwidth=4 fileencoding=utf-8

from django.contrib.sites import models as sites_models

from django.conf import settings

def site(request):
    return {
        'site': sites_models.Site.objects.get_current(),
    }

def analytics(request):
    return {
        'GA_ACCOUNT_NUM': getattr(settings, 'GA_ACCOUNT_NUM', None) if not settings.DEBUG else None
    }

# EOF

