from kivy.uix.label import Label

from home.gui.views.widgets import BaseWidget


class ModelLabel(Label, BaseWidget):

    def __init__(self, **kwargs):
        BaseWidget.__init__(self, **kwargs)
        Label.__init__(self, **kwargs)

        # super(ModelLabel, self).__init__(**kwargs)
