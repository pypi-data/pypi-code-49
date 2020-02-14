def suap_ead(request):
    if 'suap_ead' in request.session:
        return {'suap_ead': request.session['suap_ead']}
    return {'suap_ead': None}
