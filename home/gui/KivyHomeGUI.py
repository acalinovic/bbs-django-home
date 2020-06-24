import os

import django
from django.core.exceptions import ImproperlyConfigured
from django.conf import settings
from django.db.models import Model
from kivy.app import App
from kivy.uix.button import Button


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bbs.settings')
django.setup()

if settings.configured:
    from home.models import Menu
    from cookbook.models import Gene, Ingredient, Recipe
    from home.gui.required import ProcessRegistry, CommandRegistry
    from home.gui.views.layout import BBSBoxLayout, BBSGridLayout
    from home.gui.views.widgets.model import ModelButton, ModelLabel
    from home.gui.views.home import HomeMenu
else:
    raise ImproperlyConfigured


root = BBSBoxLayout(uid='root_frame', orientation='vertical')
root.size_hint = (1, 1)
root.spacing = 2

wrapper = BBSBoxLayout(uid='wrapper', orientation='horizontal')

header = BBSBoxLayout(uid='header', orientation='horizontal')
header.size_hint_max_y = 40

left = BBSBoxLayout(uid='aside_left', orientation='vertical')
left.size_hint_max_x = 150
left.add_widget(Button(text='LEFT'))

main = BBSBoxLayout(uid='main', orientation='vertical')
selection = BBSGridLayout(uid='selection', rows=5, cols=5)
batches = BBSBoxLayout(uid='batches')
main.add_widget(selection)
main.add_widget(batches)

right = BBSBoxLayout(uid='aside_right', orientation='vertical')
right.size_hint_max_x = 150
right.set_disabled(True)
right.add_widget(Button(text='RIGHT'))

footer = BBSBoxLayout(uid='footer', orientation='horizontal')
footer.size_hint_max_y = 40
footer.add_widget(Button(text='FOOTER'))

root.add_widget(header)
wrapper.add_widget(left)
wrapper.add_widget(main)
wrapper.add_widget(right)
root.add_widget(wrapper)
root.add_widget(footer)


gd = ModelLabel(uid='gene_display')
gd2 = ModelLabel(uid='gene_display2')
target = 1
for model in Gene.objects.all():
    if target == 1:
        target = 0
        string = 'gene_display'
    else:
        target = 1
        string = 'gene_display2'
    bt = ModelButton(target=string, uid=f'{model.name}_bt', model=model)
    bt.text = model.name

    bt.on_press = bt.show_model_in_modal
    selection.add_widget(bt)
    ProcessRegistry.register(model)

for menu in Menu._default_manager.filter(gui_menu=True):
    app_menu = HomeMenu(uid=menu.name, model=menu)
    header.add_widget(app_menu.menu_button)


class CookbookApp(App):
    from kivy.core.window import Window
    # Window.fullscreen = 'auto'
    title = 'CookBook'

    def build(self):
        return root


if __name__ == '__main__':

    app = CookbookApp()
    app.run()
