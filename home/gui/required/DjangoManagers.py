import django.apps
from django.db.models import Model


class DjangoManagers:
    known_models = django.apps.apps.get_models(include_auto_created=True, include_swapped=True)
    print(known_models)
    print('DjangoManager invoked')

    @classmethod
    def get_manager(cls, klass: Model):
        return klass._default_manager

    @classmethod
    def get_manager_old(cls, model: object):
        found = False
        for i in cls.known_models:
            if isinstance(model, i):
                for guess in ['objects', 'repository', 'manager']:
                    try:
                        manager = getattr(i, guess)
                        found = True
                        return getattr(i, guess)
                    except:
                        raise ModuleNotFoundError(f'no manager configured for {i}')
        if not found:
            raise ModuleNotFoundError(f'''
{model} is not a django ORM managed Model, \
verify if containing app is well registered \
in INSTALLED_APPS
''')

    @classmethod
    def get_managed_class(cls, model):
        found = False
        for i in cls.known_models:
            if isinstance(model, i):
                found = True
                return i
        if not found:
            raise ModuleNotFoundError(f'''
{model} is not a django ORM managed Model, \
verify if containing app is well registered \
in INSTALLED_APPS
''')
