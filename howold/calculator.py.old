#!venv/bin/python
# -*- coding: utf-8 -*-

import datetime

def calculateSeconds(dt_1, dt_2=None):
    if dt_2 is None:
        dt_2 = datetime.datetime.now()
    _timedelta = dt_2 - dt_1
    return int(_timedelta.total_seconds())

def convertToBaseMinute(seconds):
    s = seconds % 60
    m = (seconds - s) / 60
    return (m, s)

def convertToBaseHour(seconds):
    totals = convertToBaseMinute(seconds)
    m = totals[0] % 60
    h = (totals[0] - m) / 60
    return (h, m) + tuple(totals[1:])

def convertToBaseDay(seconds):
    totals = convertToBaseHour(seconds)
    h = totals[0] % 24
    D = (totals[0] - h) / 24
    return (D, h) + tuple(totals[1:])

def convertToBaseWeek(seconds):
    totals = convertToBaseDay(seconds)
    D = totals[0] % 7
    W = (totals[0] - D) / 7
    return (W, D) + tuple(totals[1:])

def convertToBaseYear(seconds):
    totals = convertToBaseWeek(seconds)
    W = totals[0] % 52
    Y = (totals[0] - W) / 52
    return (Y, W) + tuple(totals[1:])
