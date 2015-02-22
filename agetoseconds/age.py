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
    
    
    def get(self):
        self._calculate()
        report = self._conversion[Base.seconds]
        if self._base > Base.seconds:
            self._convert()
            report = self._conversion
        return report
    
    
    def _calculate(self):
        now = datetime.datetime.now()
        timedelta = now - self._birth
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
        raise NotImplementedError, "Unfinished implementation"
        #self._conversion = [ 0 for val in self._conversion[Base.seconds+1:] ]
        log.debug("converting age to base {}".format(self._base))
        for i in range(self._base):
            c_div = Age.conversionDivisors.get(i+1)
            log.debug("conversion divisor -> {0}".format(c_div))
        '''
        for i in range(self._base):
            total = self._conversion[i-1]
            log.debug("index {0} -> total: {1}".format(i, total))
            remainder = total % Age.ConversionTable.get(i+1)
            log.debug("calculated remainder -> {}".format(remainder))
            base = (total - remainder) / Age.ConversionTable.get(i+1)
            log.debug("calculated base -> {}".format(base))
            self._conversion[i] = remainder
            self._conversion[i+1] = base
            log.debug("'remainder' stored at index {}".format(i-1))
            log.debug("'base' stored at index {}".format(i))
        '''


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
    user_age.get()
    user_age.base = Base.years
    user_age.get()
