

class ModelMapper:
    model = None
    manager = None

    def get_model_by_attr(self, **kwargs):
        return self.manager.get(**kwargs)
