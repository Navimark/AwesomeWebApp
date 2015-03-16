#!/usr/bin/env python
# _*_ coding:utf-8 _*_

__author__ = 'ios-001'

'''
Database operation module.
'''

import  time,uuid,functools,threading,logging

#   Dict Object
class Dict(dict):
    '''
    Simple dict but support access as x.y style.
    >>>d1 = Dict()
    >>>d1['x'] = 100
    >>>d1.x
    100
    >>>d1.y = 200
    >>>d1['y']
    200
    >>>d2 = Dict(a=1,b=2,c='3')
    >>>d2.c
    '3'
    >>>d2['empty']
    Traceback (most recent call last):
        ...
    AttributeError:'Dict' object has no attribute 'empty'
    >>>d3 = Dict(('a','b','c'),(1,2,3))
    >>>d3.a
    1
    >>>d3.b
    2
    >>>d3.c
    3
    '''

    def __init__(self,names=(),values=(),**kwargs):
        super(Dict,self).__init__(**kwargs)
        for k,v in zip(names,values):
            self[k] = v

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % item)

    def __setattr__(self, key, value):
        self[key] = value

def next_id(t = None):
    '''
    Return next id as 50-char string.
    :param t: unix timestamp,default to None and using time.time().
    '''
    if t is None:
        t = time.time()