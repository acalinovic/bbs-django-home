
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown

from home.gui.required import ProcessRegistry, WidgetRegistry, CommandRegistry
from cookbook.models import *
from home.gui.views.widgets.model import ModelWidget, ModelButton


class HomeMenu(ModelWidget):
    menu_button = None
    dropdown = None

    def __init__(self, **kwargs):
        ModelWidget.__init__(self, **kwargs)
        import home.gui.commands.home_commands
        import cookbook.commands
        dropdown = DropDown()
        self.menu_button = Button()
        self.menu_button.size_hint_max_x = 150
        self.menu_button.text = self.model.label
        self.menu_button.bind(on_release=dropdown.open)
        for i in self.model.commands.all():
            button = ModelButton(uid=f'{self.model.name}_{i.name}', model=i, text=i.label, size_hint_y=None, height=34)
            dropdown.add_widget(button)
            button.bind(on_release=lambda btn: dropdown.select(btn))
        dropdown.bind(on_select=lambda instance, btn: eval(btn.model.command))
        self.dropdown = dropdown
