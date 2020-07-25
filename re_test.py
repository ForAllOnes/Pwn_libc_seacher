#!/usr/bin/env python
# coding=utf-8
import re
def get_func(func_name,text):
    offset = get_specific_func(func_name,text)
    if offset == []:
        print 'specific find not found.'
        print 'finding all funcs contains func_name'
        offset = get_all_func(func_name,text)
        if len(offset)>=2:
            for i,j in enumerate(offset):
                print j.split(' ')[0], i
            number = input('please select a number:\n')
            return int ( '0x'+offset[number].split(' ')[1] , 16)
    elif len(offset) == 1:
        return int ( '0x'+offset[0].split(' ')[1] , 16)
    return int('0x'+offset.split(' ')[1], 16)
def get_all_func(func_name,text):
    r = '[\w]*' + func_name+'[\w]* [0-9a-zA-Z]+'
    ret = re.compile(r)
    return ret.findall(text)
def get_specific_func(func_name,text):
    r = r'\n'+func_name+' [0-9a-zA-Z]+'
    ret = re.compile(r)
    a = ret.findall(text)
    if len(a)>=2:
        if a == [a[0]*len(a)]:
            return [a[0]]
    elif len(a)==1:
        return [a[0].strip()]
    return []
if __name__=="__main__":
    with open("./saved.file",'r') as f:
        text = f.read()
        while(True):
             func_name = raw_input()
             offset = get_func(func_name,text)
             print '\n', hex(offset)
