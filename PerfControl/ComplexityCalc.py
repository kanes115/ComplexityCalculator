from PerfControl.ArgData import ArgData, ArgDataImpl
from PerfControl.PerformanceControllerException import PerformanceControllerException
from PerfControl.Logger import logger
from PerfControl.Timeout import timeout
from timeit import Timer
import math
import numpy
import copy



def bladkwadr(listt):
    avg = sum(listt) / len(listt)

    licz = 0
    for i in listt:
        licz += (i - avg) * (i - avg)
    return licz



class ComplexityCalc:

    SCALE = 2
    TEST_RANGE = range(9, 18)
    COMPLEXITITES = {'O(logn)': lambda N, time: time / math.log2(N),
                     'O(nlogn)': lambda N, time: time / N / math.log2(N),
                     'O(n)': lambda N, time: time / N, 'O(n^2)': lambda N, time: time / (N * N),
                     'O(n^3)': lambda N, time: time / (N * N * N)}

    def __init__(self, func, arg, maxtime_sec=1000, repeat=1):
        if not callable(func) or ArgData not in arg.__class__.__bases__:
            raise PerformanceControllerException("Invalid arguments.")

        self.test_algorithm = func
        self.test_arg = arg
        self.timeout = maxtime_sec
        self.measures = dict()
        self.complexity = None
        self.SIZES = [pow(self.SCALE, i) for i in self.TEST_RANGE]                   # must be sorted
        self.repeat = repeat
        self.constance = 1

    def calculate_complexity(self):
        measures = self.get_measures()
        errors = self.count_errors(measures)
        minc = ('', float('inf'))
        for complexity_name, (std, mean) in errors.items():
            if std < minc[1]:
                minc = (complexity_name, std, mean)
        self.complexity = minc[0]
        self.constance = mean
        # print('For function: ' + self.test_algorithm.__name__())
        return minc[0]

    # returns: dictionary N -> time
    @timeout()
    def get_measures(self):
        measures = dict()
        prev = 0            # previous size
        self.test_arg.set_data(0)
        progress = 1
        for i in self.SIZES:
            for _ in range(self.accuracy):
                self.test_arg.inc_data(i - prev)
                prev = i
                rawdata_copy = copy.deepcopy(self.test_arg.get_raw_data())

                print('counting for ' + str(i))
                print(str(int(progress * 100 / len(self.TEST_RANGE) / self.accuracy)) + '% progress...')

                t = Timer(lambda: self.test_algorithm(rawdata_copy))
                measures[i] = t.timeit(number=1)
                progress += 1
        self.measures = measures
        return measures

    # returns: dictionary COMPLEXITY -> wariancja
    def count_errors(self, measures):
        res = dict()
        for name, f in self.COMPLEXITITES.items():
            vals = []
            for N, time in measures.items():
                vals.append(f(N, time))
            res[name] = (numpy.std(vals) / numpy.mean(vals), numpy.mean(vals))
        return res

    def forecast(self, size):








def mysum(arglist):
    sum = 0
    for i in arglist:
        sum += i
    return sum

def mysum_sq(arglist):
    sum = 0
    for i in arglist:
        for j in arglist:
            sum += i * j
    return sum


def quicksort(list):
    if not list:
        return []
    else:
        tmp = list[0]
        less = [x for x in list if x <  tmp]
        more = [x for x in list[1:] if x >= tmp]
        return quicksort(less) + [tmp] + quicksort(more)


def sure_nlogn(arglist):
    N = len(arglist)
    sum = 0
    for i in range(int(N * math.log2(N))):
        sum += arglist[i % N]
    return sum


def main():
    a = ArgDataImpl([1,2,3,4])
    try:
        A = ComplexityCalc(quicksort, a, 10000)
        print(A.calculate_complexity())
    except PerformanceControllerException as e:
        print(str(e))
        exit(-1)

main()