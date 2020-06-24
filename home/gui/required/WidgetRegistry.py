from kivy.uix.widget import Widget


class WidgetRegistry:
    print('widget registry invoked')
    _global_widgets = dict()

    @classmethod
    def register(cls, instance: Widget):
        if not cls._global_widgets.get(instance.uid):
            cls._global_widgets[instance.uid] = instance

    @classmethod
    def unregister(cls, widget):
        try:
            cls._global_widgets.pop(widget.uid)
        except KeyError:
            pass

    @classmethod
    def select(cls, uid: str):
        try:
            return cls._global_widgets[uid]
        except KeyError:
            raise KeyError(f'id \'{uid}\' does not exists in {WidgetRegistry}')

    @classmethod
    def widgets(cls):
        return cls._global_widgets
