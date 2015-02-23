from __future__ import print_function

import datetime
import logging


class Base:
    seconds, minutes, hours, days, weeks, years = range(6)


class Age(object):
    def __init__(self, year, month, day, hour=0, minute=0, second=0):
        self._birth = datetime.datetime(year, month, day, hour, minute, second)
        self._conversion = [0]*6
        self._base = Base.seconds
    
    
    @property
    def base(self):
        return self._base
    
    
    @base.setter
    def base(self, unit):
        assert unit >= Base.seconds
        assert unit <= Base.years
        self._base = unit
    
    
    def tick(self):
        self._calculate()
        report = self._conversion[Base.seconds]
        if self._base > Base.seconds:
            self._convert()
            report = tuple(self._conversion[:self._base+1])
        return report
    
    
    def _calculate(self):
        now = datetime.datetime.now()
        timedelta = now - self._birth
        self._conversion = [ 0 for val in self._conversion ]
        self._conversion[Base.seconds] = int(timedelta.total_seconds())
        log.debug("calculated timedelta -> {} seconds ".format(self._conversion[Base.seconds]))
    
    
    conversionDivisors = {
        Base.seconds + 1 : 60,
        Base.minutes + 1 : 60,
        Base.hours + 1   : 24,
        Base.days + 1    : 7,
        Base.weeks + 1   : 52
    }
    
    
    def _convert(self):
        self._conversion = [ 0 if n > Base.seconds else val for n, val in enumerate(self._conversion)  ]
        log.debug("converting to base {}".format(self._base))
        for i in range(self._base):
            if i == Base.years:
                break
            c_div = Age.conversionDivisors.get(i+1)
            total = self._conversion[i]
            remainder = total % c_div
            base_val = (total - remainder) / c_div
            self._conversion[i] = remainder
            self._conversion[i+1] = base_val
            
            log.debug("iteration = {}".format(i))
            log.debug(" get 'total' from index {0} -> {1}".format(i, total))
            log.debug(" mod {0} division : value 'remaining' -> {1}".format(c_div, remainder))
            log.debug(" integer division by {0} : value 'base' -> {1}".format(c_div, base_val))
            log.debug(" index: {0}  {1}  ...".format(' '*(len(str(remainder))-1) + str(i), ' '*(len(str(base_val))-1) + str(i+1)))
            log.debug(" array: {0}, {1}, ...".format(remainder, base_val))


if __name__ == "__main__":
    
    import sys
    try:
        import logging
    except:
        raise
    
    loglevels = {
        'debug'     : logging.DEBUG,
        'info'      : logging.INFO,
        'warning'   : logging.WARNING,
        'error'     : logging.ERROR,
        'critical'  : logging.CRITICAL,
    }
    
    if len(sys.argv) > 1:
        loglevel = loglevels.get(sys.argv[1], logging.NOTSET)
        logging.basicConfig(level=loglevel)
    log = logging.getLogger(__name__)
    
    user_age = Age(1986, 8, 18, 16, 55, 45)
    report = user_age.tick()
    log.info(report)
    user_age.base = Base.years
    report = user_age.tick()
    log.info(report)
    user_age.base = Base.minutes
    report = user_age.tick()
    log.info(report)
