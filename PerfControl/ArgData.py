import random
from abc import ABC, abstractmethod
from PerfControl.Logger import logger


class ArgData(ABC):

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


class ArgDataImpl(ArgData, list):

    def __init__(self, listt):
        self.listt = listt
        super(ArgDataImpl, self).__init__(listt)

    def set_data(self, amount):
        self.listt = [random.randint(0, 1000) for r in range(amount)]

    def inc_data(self, amount):
        extra = [random.randint(0, 1000) for r in range(amount)]
        self.listt += extra

    def get_data_size(self):
        return len(self.listt)

    def get_raw_data(self):
        return self.listt
