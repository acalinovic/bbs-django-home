from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.widget import Widget

from home.gui.controllers import ModelMapperFactory
from home.gui.required import WidgetRegistry


class ModelWidget(Widget):
    uid = StringProperty()
    model = ObjectProperty()
    mapper = ObjectProperty()
    manager = ObjectProperty()

    def __init__(self, **kwargs):
        try:
            self.uid = kwargs.pop('uid')
        except KeyError:
            raise KeyError(f'instance {self} must have an "uid" argument')
        WidgetRegistry.register(self)
        self.model = kwargs.pop('model')
        self.mapper = ModelMapperFactory(self.model).get_mapper()
        self.manager = self.mapper.manager

        Widget.__init__(self, **kwargs)
