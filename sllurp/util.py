from __future__ import unicode_literals
from inspect import stack
import re

from twisted.internet.defer import Deferred

def BIT(n):
    return 1 << n


def BITMASK(n):
    return ((1 << (n)) - 1)


def func():
    "Return the current function's name."
    return stack()[1][3]


def reverse_dict(data):
    atad = {}
    for m in data:
        i = data[m]
        atad[i] = m
    return atad


def atoi(text):
    return int(text) if text.isdigit() else text


def natural_keys(text):
    """Sort alphanumerics in a "natural" order
    Source: https://stackoverflow.com/questions/5967500/

    >>> sorted(['foo25', 'foo3'], key=natural_keys)
    ['foo3', 'foo25']
    """
    return [atoi(c) for c in re.split('(\d+)', text)]

def run_async(func, *args, **kwargs):
    """
    Run callback-style function and return corresponding Deferred object.

    :param func: Function to run
    :param args: Arguments to be passed to the function
    :param kwargs: Keyword arguments to be passed to the function
    :returns: Deferred object
    """
    d = kwargs.setdefault("onCompletion", Deferred())
    # Call function with deferred object
    func(*args, **kwargs)
    # Return deferred object
    return d
