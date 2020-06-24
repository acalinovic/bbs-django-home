from kivy.properties import StringProperty
from kivy.uix.widget import Widget

from home.gui.required import WidgetRegistry


class BaseWidget(Widget):
    uid = StringProperty()

    def __init__(self, **kwargs):
        try:
            self.uid = kwargs.pop('uid')
        except KeyError:
            raise KeyError(f'instance {self} must have an "uid" argument')
        WidgetRegistry.register(self)
        Widget.__init__(self, **kwargs)
