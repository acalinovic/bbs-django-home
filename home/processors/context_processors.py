from home.models import Menu


def app_menus(request):
    all_menus = dict()
    all_menus['menus'] = Menu.repository.filter(parent=None)

    return all_menus
