from __future__ import print_function

import datetime
import logging


log = logging.getLogger(__name__)


class Unit:
    seconds, minutes, hours, days, weeks, years = range(6)


class Age(object):
    """Represents any age by wrapping around a python datetime.
    """
    
    def __init__(self, date_object, time_object=None, **kwargs):
        self._dateObject = date_object
        if not time_object:
            time_object = datetime.time()
        self._timeObject = time_object
        self._age = datetime.datetime.combine(self._dateObject, self._timeObject)
        self._conversion = [0]*6
        self._unit = Unit.seconds
    
    # map unit literals to a unit enumeration value
    units = {
            'seconds': Unit.seconds,
            'minutes': Unit.minutes,
            'hours': Unit.hours,
            'days': Unit.days,
            'weeks': Unit.weeks,
            'years': Unit.years,
            }


    @property
    def unit(self):
        return self._unit


    @unit.setter
    def unit(self, unit):
        assert unit in Age.Units
        #assert unit >= Unit.seconds
        #assert unit <= Unit.years
        self._unit = Age.Units.get(unit)


    def get(self):
        '''This method returns your age as an integer or tuple value
        
        By default, this method will return an integer counting the
        age in seconds.
        
        When the 'unit' property was set to a unit of a higher rank,
        this method returns a tuple.
        The first element in the tuple is the unit specified. Each 
        consecutive element is the value of the next lower ranked unit,
        down to seconds.
        '''
        self._conversion = [ 0 for val in self._conversion ]
        self._conversion[Unit.seconds] = self._calculate()
        report = self._conversion[Unit.seconds]
        if self._unit > Unit.seconds:
            self._convert()
            report = tuple(self._conversion[:self._unit+1])
        return report


    def setTime(self, time_object=None, **kwargs):
        """Sets the internal time object after object creation.
        
        Keyword arguments precede the positional argument.
        
        Keyword arguments:
          hour:   Positive integer
          minute: Positive integer
          second: Positive integer
        """
        if kwargs:
            arguments = [ kwargs.get(k) if k in kwargs else 0 for k in ('hour','minute','second') ]
            time_object = datetime.time(*arguments)
        if not time_object:
            time_object = datetime.time()
        self._timeObject = time_object
        self._age = datetime.datetime.combine(self._dateObject, self._timeObject)


    def _calculate(self):
        now = datetime.datetime.now()
        timedelta = now - self._age
        result = int(timedelta.total_seconds())
        log.debug("calculated timedelta -> {} seconds ".format(self._conversion[Unit.seconds]))
        return result

    
    # Divisors are used in the conversion algorithm and can be indexed
    # with unit enumeration values
    conversionDivisors = {
        Unit.seconds+1: 60,
        Unit.minutes+1: 60,
        Unit.hours+1: 24,
        Unit.days+1: 7,
        Unit.weeks+1: 52
        }


    def _convert(self):
        self._conversion = [ 0 if n > Unit.seconds else val for n, val in enumerate(self._conversion)  ]
        log.debug("converting to unit {}".format(self._unit))
        for i in range(self._unit):
            if i == Unit.years:
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
            log.debug(" integer division by {0} : value 'unit' -> {1}".format(c_div, base_val))
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
