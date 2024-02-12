import math
import sys


def arange(no_sample):
    """
    arange
    Generates a list of numbers from 0 to target value with increment of 1

    args:
    no_sample: The number of values to generate
    """
    l_ = []
    for i in range(no_sample):
        l_.append(i)
    return l_

def scale_list(l):
    new =[]
    length = len(l)
    max_ = max(l)
    min_ = min(l)
    for i in range(length):
        new.append((l[i]-min_)/(max_ - min_))
    return new


def max_index(l):
    '''
    max_index
    Function that accepts a list 1-d and returns the index of the element with the
    maximum value.
    
    args:
    l: A list that is passed whose max-idex is to be found out 
    '''
    max_ = 0
    idx = 0
    for i in range(len(l)):
        if abs(l[i])>max_:
            max_ = abs(l[i])
            idx = i
        
    return idx


def min_index(l):
    '''
    min_index
    Function that accepts a list 1-d and returns the index of the element with the
    minimum value.
    
    args:
    l: A list that is passed whose min-idex is to be found out 
    '''
    min_ = 1e300
    idx = 0
    for i in range(len(l)):
        if abs(l[i])<min_:
            min_ = abs(l[i])
            idx = i
        
    return idx

def init_list(length, mode = "zero", constant = 0):
    '''
    init_list 
    Funtion that initialises a list as per a given mode
    
    args:
    length: The length of the list to be initialised
    mode: The mode of initialization
    constant: A scalar passed for initialization with constant values
    
    Supported modes-
    zero:- Initialize with all zeros
    constant:- Initialize will all elements equal to the constant passed
    '''
    if mode == "zero":
        l = []
        for i in range(length):
            l.append(0)
    if mode == "constant":
        l = []
        for i in range(length):
            l.append(constant)

    return l
