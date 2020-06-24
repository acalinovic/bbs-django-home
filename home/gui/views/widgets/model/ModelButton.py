from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup

from home.gui.controllers import ModelMapperFactory
from home.gui.required import WidgetRegistry


class ModelButton(Button):
    uid = StringProperty()
    target = ObjectProperty()
    model = ObjectProperty()
    mapper = ObjectProperty
    manager = ObjectProperty()

    def __init__(self, **kwargs):
        self.model = kwargs.pop('model')
        if kwargs.get('target'):
            self.target = WidgetRegistry.select(kwargs.pop('target'))
        try:
            self.uid = f'{self.model.__class__.__name__}_{str(self.model.id)}'
        except KeyError:
            raise KeyError(f'instance {self} must have an "uid" argument')
        WidgetRegistry.register(self)
        self.mapper = ModelMapperFactory(self.model).get_mapper()
        self.manager = self.mapper.manager

        Button.__init__(self, **kwargs)

    def print_model_name(self):
        self.target.text = self.model.name

    def add_model_to_process(self):
        self.target.add_widget(Label(text=self.model.name))

    def show_model_in_modal(self):
        popup = Popup(title='Test popup',
                      auto_dismiss=False,
                      size_hint=(None, None), size=(400, 400))
        root = BoxLayout(orientation='vertical')
        label = Label(text=self.model.name)
        button = Button(text='close')
        button.size_hint_max_y = 40
        button.bind(on_press=popup.dismiss)
        root.add_widget(label)
        root.add_widget(button)
        popup.content = root

        popup.open()
