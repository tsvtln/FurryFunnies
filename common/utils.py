def create_author_profile(request):
    request.session['has_author_profile'] = True


def author_profile_status(request):
    has_profile = request.session.get('has_author_profile', False)
    return {'has_author_profile': has_profile}
