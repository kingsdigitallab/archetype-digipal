from django.shortcuts import redirect

def redirect_view(request, *args, **kwargs):
    '''Usage: 
        To redirect /the/old/path/page1 to /the/new/path/page1, add the following line to urls.py  
        
        (r'^the/old/path/(.*)', 'digipal_django.redirect_views.redirect_view', {'new_path': r'/the/new/path/\1'}),
    '''
    import re
    new_path = kwargs['new_path']
    i = 0
    for arg in args:
        i += 1
        new_path = new_path.replace(r'\%s' % i, arg)
    return redirect(new_path)

