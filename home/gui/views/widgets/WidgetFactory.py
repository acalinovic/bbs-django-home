from kivy.uix import dropdown

from home.gui.required import WidgetRegistry, ProcessRegistry


class WidgetFactory:
    klass = None
    kwargs = None
    widget = None

    def __init__(self, **kwargs):
        try:
            self.klass = kwargs.pop('klass')
            self.kwargs = kwargs
        except KeyError:
            raise KeyError(f'klass argument is mandatory !')

        self.widget = self.klass.__new__(self.klass, **kwargs)

        if isinstance(self.widget, dropdown.DropDown):
            setattr(self.widget, 'uid', kwargs.get('uid'))

        WidgetRegistry.register(self.widget)

    def get_widget(self):
        return self.widget
