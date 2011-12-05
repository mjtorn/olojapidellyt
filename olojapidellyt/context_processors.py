# vim: tabstop=4 expandtab autoindent shiftwidth=4 fileencoding=utf-8

from django.contrib.sites import models as sites_models

def site(request):
    return {
        'site': sites_models.Site.objects.get_current(),
    }

# EOF

