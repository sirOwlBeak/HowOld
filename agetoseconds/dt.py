#!venv/bin/python
# -*- coding: utf-8 -*-

import datetime
try:
    import cPickle as pickle
except:
    import pickle

_FILENAME = "user.pickle"

def storeDatetime(datetime_obj):
    with open(_FILENAME, 'wb') as output_file:
        pickle.dump(datetime_obj, output_file)

def loadDatetime():
    with open(_FILENAME, 'rb') as input_file:
        obj = pickle.load(input_file)
    return obj

def newDatetime(Y, M, D, h=0, m=0, s=0):
    _dt = datetime.datetime(Y, M, D, h, m, s, 0)
    return _dt
