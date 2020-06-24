class ProcessRegistry:
    print('process registry invoked')
    _global_objects = dict()

    @classmethod
    def register(cls, instance: object):
        uid = f'{type(instance).__name__}_{instance.id}'
        if not cls._global_objects.get(uid):
            cls._global_objects[uid] = instance

    @classmethod
    def unregister(cls, instance: object):
        uid = f'{type(instance).__name__}_{instance.id}'
        try:
            cls._global_objects.pop(uid)
        except KeyError:
            pass

    @classmethod
    def get(cls, uid: str):
        try:
            return cls._global_objects[uid]
        except KeyError:
            raise KeyError(f'id \'{uid}\' does not exists in {ProcessRegistry}')

    @classmethod
    def objects(cls):
        return cls._global_objects

    @classmethod
    def objects_by_type(cls, typ: type):
        export = dict()
        for k, v in cls._global_objects.items():
            if isinstance(v, typ):
                export[k] = v
        return export

    @classmethod
    def pop(cls, uid: str):
        return cls._global_objects.pop(uid)

    @classmethod
    def pop_all(cls, typ: type):
        export = dict()
        for k, v in cls._global_objects.items():
            if isinstance(v, typ):
                export[k] = v
        for k, v in export.items():
            cls._global_objects.pop(k)
        return export

    @classmethod
    def get_object_by_attr(cls, obj: type, **kwargs):
        export = dict()
        for k, v in cls._global_objects.items():
            if isinstance(v, obj):
                for attr, value in kwargs.items():
                    try:
                        if getattr(v, attr) == value:
                            export[k] = v
                    except:
                        pass
        if len(export) == 0:
            return None
        elif len(export) == 1:
            return [i for i in export.values()][0]
        else:
            return export
