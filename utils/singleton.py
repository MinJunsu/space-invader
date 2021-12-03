class SingletonInstance:
    _instance = None

    @classmethod
    def _get_instance(cls):
        return cls._instance

    @classmethod
    def instance(cls, *args, **kwargs):
        cls.__instance = cls()
        cls.instance = cls._get_instance()
        return cls._instance
