import random
from abc import abstractmethod


class ArgData:
    '''
    Abstract class that a class has to inherit from
    in order to be able to be passed to ComplexityCalc
    as input data. It provides methods to increase
    the input data size (by random data, preferably),
    set data size for a particular size, get raw data
    so that it can be used in algorithm.
    '''

    @abstractmethod
    def set_data(self, amount):
        pass

    @abstractmethod
    def inc_data(self, amount):
        pass

    @abstractmethod
    def get_data_size(self):
        pass

    @abstractmethod
    def get_raw_data(self):
        pass


class ArgDataListImpl(ArgData, list):
    '''
    Example of implementation of ArgData
    '''

    def __init__(self, listt):
        self.listt = listt
        super(ArgDataListImpl, self).__init__(listt)

    def set_data(self, amount):
        self.listt = [random.randint(0, 1000) for _ in range(amount)]

    def inc_data(self, amount):
        extra = [random.randint(0, 1000) for _ in range(amount)]
        self.listt += extra

    def get_data_size(self):
        return len(self.listt)

    def get_raw_data(self):
        return self.listt
