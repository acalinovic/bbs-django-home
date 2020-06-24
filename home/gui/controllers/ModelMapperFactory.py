from . ModelMapper import ModelMapper
from home.gui.required.DjangoManagers import DjangoManagers


class ModelMapperFactory:
    mapper = None

    def __init__(self, model, **kwargs):
        self.mapper = ModelMapper()
        self.mapper.model = DjangoManagers.get_managed_class(model)
        self.mapper.manager = DjangoManagers.get_manager(self.mapper.model)

    def get_mapper(self):
        return self.mapper
