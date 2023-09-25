from abc import ABCMeta, abstractmethod


class Programa(metaclass = ABCMeta):
    @abstractmethod
    def __str__(self):
        pass

class Algo(Programa):
    def __str__(self):
        pass

algo = Algo()