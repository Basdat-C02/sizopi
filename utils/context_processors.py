def username_and_role(request):
    username = request.session.get('username', 'Guest')
    role = request.session.get('role', None)

    return {
        'username': username,
        'role': role,
    }