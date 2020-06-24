from kivy.uix.boxlayout import BoxLayout

from home.gui.views.widgets import BaseWidget


class BBSBoxLayout(BoxLayout, BaseWidget):

    def __init__(self, **kwargs):
        BaseWidget.__init__(self, **kwargs)
        BoxLayout.__init__(self, **kwargs)

        # super(BBSBoxLayout, self).__init__(**kwargs)
