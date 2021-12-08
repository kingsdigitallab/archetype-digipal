import sys

# TODO !
DEBUG = True

SHOW_QUICK_SEARCH_SCOPES = True

LIGHTBOX = True

if 1:
    ALLOWED_HOSTS = [
        '.digipal.eu', # Allow domain and subdomains
        'digipal2.cch.kcl.ac.uk',
        'digipal.cch.kcl.ac.uk',
    ]

# ADMIN_FORCE_HTTPS = True

REJECT_HTTP_API_REQUESTS = True
API_PERMISSIONS = [['r', 'ALL'], ['', 'description,stewartrecord,handdescription,requestlog,carouselitem,user']]

HIDDEN_ADMIN_APPS = ('digipal', )

ADMINS = []
# AC-10 (digipal)
# SERVER_EMAIL = 'no-reply@kcl.ac.uk'
# EMAIL_HOST = 'smtp.cch.kcl.ac.uk'

MODELS_PUBLIC = ['itempart', 'image', 'graph', 'hand', 'handdescription', 'scribe']
MODELS_PRIVATE = ['itempart', 'image', 'graph', 'hand', 'handdescription', 'scribe']

KDL_MAINTAINED = True

BANNER_LOGO_HTML = '''
<span id="logo">
    <span class="logo-brand logo-brand-digi">Digi</span><span class="logo-brand logo-brand-pal">Pal</span><span class="logo-separator hidden-sm hidden-xs">&nbsp;</span><span class="logo-sub hidden-sm hidden-xs">
        Digital Resource and Database of Palaeography,
        <br>
        Manuscript Studies and Diplomatic
    </span>
</span>
'''
