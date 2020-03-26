# coding: UTF-8

class Singleton(object):
    """
    これを継承したclassはシングルトンになる
    """
    def __new__(cls, *_, **__):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance