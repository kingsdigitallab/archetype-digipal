# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings

# Mapping of the URLs from the old Wordpress website to this website
# Place the most specific paths first (e.g. A/B before A),
# otherwise they will be ignored.
mappings = [
             [r'^blog/describing-handwriting-part-ii/(.*)', r'/blog/describing-handwriting-part-ii-terminology/\1'],
             [r'^blog/describing-handwriting-part-iii/(.*)', r'/blog/describing-handwriting-part-iii-hands-and-graphs/\1'],
             [r'^blog/describing-handwriting-part-iv/(.*)', r'/blog/describing-handwriting-part-iv-recapitulation-and-formal-model/\1'],
             [r'^blog/describing-handwriting-part-v/(.*)', r'/blog/describing-handwriting-part-v-english-vernacular-minuscule/\1'],
             [r'^blog/describing-handwriting-part-vi/(.*)', r'/blog/describing-handwriting-part-vi-the-model-in-action/\1'],
             [r'^blog/referring-to-scribal-hands/(.*)', r'/blog/referring-to-scribal-hands-an-open-question/\1'],
             [r'^blog/second-symposium-followup/(.*)', r'/blog/tweeting-the-second-symposium/\1'],
             #[r'^blog/.*digital-resources-for-palaeography.*?one-day-symposium/(.*)', r'/blog/digital-resources-for-palaeography-one-day-symposium/\1'],
             [r'^blog/.digital-resources-for-palaeography.-one-day-symposium/(.*)', r'/blog/digital-resources-for-palaeography-one-day-symposium-info/\1'],
             [r'^blog/digital-resources-for-palaeography-one-day-symposium/(.*)', r'/blog/cfp-digital-resources-for-palaeography-one-day-symposium/\1'],
             [r'^blog/bl-labs/(.*)', r'/blog/bl-labs-launch-palaeographers-speak-with-forked-ascenders/\1'],
             [r'^blog/digipal-cfp/(.*)', r'/blog/digipal-call-for-papers-digital-approaches-to-medieval-script-and-image/\1'],
             [r'^blog/phd-studentship-digital-resource-of-palaeography/(.*)', r'/blog/phd-studentship-digital-resource-for-palaeography/\1'],
             [r'^blog/programme/(.*)', r'/blog/update-programme-for-digital-approaches-to-medieval-script-and-image-symposium/\1'],
             [r'^blog/quadrivium-viii/(.*)', r'/blog/quadrivium-viii-phd-training-on-manuscripts-and-digital-humanities/\1'],
             [r'^blog/symposium-update/(.*)', r'/blog/update-list-of-speakers-for-the-digital-approaches-to-medieval-script-and-image-symposium/\1'],
             [r'^blog/xviiie-colloque-international-de-paleographie-latine-st-gall-11-14-sept-2013/(.*)', ur'/blog/xviiie-colloque-international-de-paleographie-latine-st-gall-1114-sept-2013/\1'],

             [r'^blogs/(\d{4})/(\d{2})', r'/blog/archive/\1/\2'],
             [r'^blogs/blog/(.*)', r'/blog/\1'],
             [r'^blog/news/(.*)', r'/blog/\1'],
             [r'^blogs/(.*)', r'/blog/\1'],
             [r'^blog-2/(.*)', r'/blog/\1'],
             [r'^search/(.*)', r'/digipal/search/\1'],
             [r'^news/(.*)', r'/blog/category/news/\1'],
             [r'^about/?$', r'/about/digipal/'],
             [r'^resources/(.*)', r'/glossary/\1'],
             # See JIRA 482
             #[r'^about/project-rationale/(.*)', r'/about/the-project/\1'],
             [r'^about/references/(.*)', r'/general-bibliography/\1'],
             [r'^about/feedback/(.*)', r'/about/contact/\1'],
             [r'^contact/(.*)', r'/about/contact-us/\1'],
            ]

def get_redirect_patterns():
    ret = None
    for mapping in mappings:
        pattern = patterns('', (mapping[0], '%s.redirect_views.redirect_view' % settings.PROJECT_DIRNAME, {'new_path': mapping[1]}))
        if ret is None:
            ret = pattern
        else:
            ret += pattern

    return ret

def get_redirected_url(url, unchanged_if_not_found=False, return_absolute=False):
    # r = get_redirected_url('http://www.digipal.eu/blogs/blog/the-problem-of-digital-dating-part-i/')
    # r = /blog/the-problem-of-digital-dating-part-i/
    #
    # query strings are ignored
    # The original domain is left unchanged if return_absolute = True or unchanged_if_not_found
    # otherwise a relative path is return
    #
    import re
    from urlparse import urlsplit
    path_parts = urlsplit(url)
    prefix = ur'%s://%s' % (path_parts.scheme, path_parts.netloc)
    path = path_parts.path

    # remove leading /
    ret = re.sub(ur'^/', '', path)
    #ret = path[1:]
    amappings = mappings[:]
    ret0 = ret
    while True:
        if not len(amappings): break
        mapping = amappings.pop(0)
        ret = re.sub(mapping[0], mapping[1], ret)
        if ret != ret0:
            ret = re.sub(ur'^/', '', ret)
            # retry mapping from the first one
            ret0 = ret
            amappings = mappings[:]

    if not ret or ret[0] != '/': ret = '/' + ret

    if unchanged_if_not_found:
        # does this path exists here?
        from django.core.validators import URLValidator
        from django.core.exceptions import ValidationError
        from django.contrib.sites.models import Site
        current_site = Site.objects.get_current()
        validate = URLValidator(verify_exists=True)
        absolute_url = 'http://' + current_site.domain + ret

#         from django.core.urlresolvers import resolve, Resolver404
#         try:
#             print u'resolve ' + ret
#             r = resolve(ret)
#             print r
#         except Resolver404:
#             print u'NOT FOUND'
#             ret = url

        try:
            validate(absolute_url)
        except ValidationError, e:
            #print u'NOT FOUND (%s)' % absolute_url
            ret = url

    if return_absolute and not re.search('http.?:', ret):
        ret = prefix + ret

#        try:
#            validate(absolute_url)
#        except ValidationError, e:
#            print 'ERROR'
#            print e
#            ret = url

    return ret
