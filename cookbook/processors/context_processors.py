from django.http import HttpRequest


def site_vars(request: HttpRequest):
    return {'app_menus': None}
