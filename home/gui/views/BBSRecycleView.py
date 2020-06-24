from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView

from home.gui.required import WidgetRegistry
from home.gui.views.widgets import BaseWidget
from home.gui.views.widgets.model import ModelWidget


class BBSRecycleView(RecycleView):

    def __init__(self, **kwargs):
        Builder.load_string(f'''
<BBSRecycleView>:
    id: {kwargs.pop('uid')}
    viewclass: 'ModelButton'

    RecycleBoxLayout:
        default_size: None, dp(56)
        default_size_hint: 1, None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'
        multiselect: True
        touch_multiselect: True
        ''')
        data = kwargs.pop('data')
        model = kwargs.pop('model')
        super(BBSRecycleView, self).__init__(**kwargs)
        WidgetRegistry.register(self)
        self.data = data
