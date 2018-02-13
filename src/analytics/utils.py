def get_client_ip(request):
    """ There`a a chance that we might not get ip address
    if these headers aren`t there
    """

    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip