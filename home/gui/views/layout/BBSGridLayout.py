from kivy.uix.gridlayout import GridLayout

from home.gui.views.widgets import BaseWidget


class BBSGridLayout(GridLayout, BaseWidget):

    def __init__(self, **kwargs):
        BaseWidget.__init__(self, **kwargs)
        GridLayout.__init__(self, **kwargs)

        # super(BBSGridLayout, self).__init__(**kwargs)
