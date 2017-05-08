import signal
from .PerformanceControllerException import PerformanceControllerException

#   This is a decorator that timeouts methods
#   A class has to have defined a field called "timeout"


class TimeoutExceededException(Exception):
    pass


def timeout():
    '''
    Decorator that when used with a method
    ensures it won't exceed amount of time
    specified in an object's timeout field
    (must be provided).
    '''
    def real_dec(func):
        def alarm_handle(signo, info):
            raise TimeoutExceededException

        def timeouted_func(*args, **kwargs):
            sec = args[0].timeout
            if not isinstance(sec, int):
                raise PerformanceControllerException(
                    "Timeout was not specified properly"
                )
            signal.signal(signal.SIGALRM, alarm_handle)
            signal.alarm(sec)
            try:
                res = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return res
        return timeouted_func
    return real_dec
