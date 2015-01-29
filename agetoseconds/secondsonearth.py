#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple

import datetime
import random
import argparse

import dt
import calculator
##
## This part sets up commandline arguments
"""
parser = argparse.ArgumentParser(description="This program calculates your age in seconds.")

parser.add_argument(
    'BIRTHDAY', 
    action = 'store',
    help = "Pass your birthday as 'DD-MM-YYYY'" 
)

parser.add_argument(
    '--time',
    '-t', 
    action = 'store',
    help = "Pass the time of your birth as 'hh:mm:ss'"
)

parser.add_argument(
    '--base',
    '-b', 
    action = 'store', 
    choices = ['Y','M','W','D','h','m','s'], 
    help = "Select the base unit in which to report your age"
)


#unit_selector = parser.add_mutually_exclusive_group()
#unit_selector.add_argument("--years", action='store_true', help='get age expressed in weeks')
#unit_selector.add_argument("--months", action='store_true', help='get age expressed in months')
#unit_selector.add_argument("--weeks", action='store_true', help='get age expressed in weeks')
#unit_selector.add_argument("--days", action='store_true', help='get age expressed in days')
#unit_selector.add_argument("--hours", action='store_true', help='get age expressed in hours')
#unit_selector.add_argument("--minutes", action='store_true', help='get age expressed in minutes')

args = parser.parse_args()
"""
reports = (
    "You have spent {0} on this planet!",
    "You have been consuming oxygen for {0}!",
    "You were spawned into this realm {0} ago!",
    "You started breathing {0} ago!",
    "You are {0} young!"
    )

## pickle friendly named tuple
Birthday = namedtuple('Birthday', ['Y','M','D','h','m','s'])


"""
## refactor
def calcTimeDelta(datetime_obj):
    return datetime.datetime.now() - datetime_obj

## refactor
def timeInSeconds(timedelta_obj):
    return "{:,d} seconds".format(int(timedelta_obj.total_seconds())).replace(',' ,'.')

## refactor    
def printLifeInSeconds(time_in_seconds):
    print "You have spent {:,d} seconds on earth!".format(time_in_seconds)
"""
""" YOUR MAIN HAS BEEN DEPRECATED SINCE >1 SECOND !
def main():
    year = 1986
    month = 8
    day = 18
    hour = 16
    minute = 45
    second = 10
    birthdate = datetime.datetime(year, month, day, hour, minute, second)
    timedelta = calcTimeDelta(birthdate)
    t = timeInSeconds(timedelta)
    out = random.choice(LIFE_PASSED)
    print out.format(t)
"""
if __name__ == "__main__":
    ## a new Birthday should be instanciated by the command line invocation, we will hardcode a Birthday for testing purposes
    #mock_birthday = Birthday(Y=1986, M=8, D=18, h=16, m=44, s=15)
    #mock_birthday = Birthday(Y=1988, M=10, D=2, h=8, m=15, s=3)
    me = dt.newDatetime(1986, 8, 18, 8, 44, 15)
    #dt = loadDatetime()
    seconds = calculator.calculateSeconds(me)
    print calculator.convertToBaseMinutes(seconds)
    print calculator.convertToBaseHours(seconds)
    print calculator.convertToBaseDays(seconds)
    print calculator.convertToBaseWeeks(seconds)
    print calculator.convertToBaseYears(seconds)
    
    
    """
    date_int = [int(n) for n in args.BIRTHDATE.split('-')] ## [day, month, year]
    time_int = [0,0,0]
    if args.time:
        time_int = [int(n) for n in args.time.split(':')] ## [hour, minutes, seconds]
    birthdate = datetime.datetime(date_int[2], date_int[1], date_int[0], time_int[0], time_int[1], time_int[2])
    timedelta = calcTimeDelta(birthdate)
    t = timeInSeconds(timedelta)
    report = random.choice(LIFE_PASSED)
    print report.format(t)
    """
