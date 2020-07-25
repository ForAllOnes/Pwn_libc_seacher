#!/usr/bin/env python
# coding=utf-8
import re

def get_func(func_name,text):
    # I don't know how to capture a stringa start with a specific stingb
    # this part need changes.
    r = '[\w]*'+func_name+'[\w]* [0-9a-zA-Z]+'
    r = re.compile(r)
    ret = r.findall(text)
    offset = get_specific_func(func_name,ret)
    while offset == None:
        for i in ret :
            print i.split(' ')[0]
        func_name = raw_input('please select a specific func_name:\n')
        return get_func(func_name, text)
    print hex(offset)
    return offset

def get_specific_func(func_name,ret):
    for i in ret:
        i = i.split(' ')
        name = i[0]
        offset = i[1]
        if name == func_name:
            print name,offset
            return int(('0x'+offset),16)
    return None

if __name__=="__main__":
    with open("./saved.file",'r') as f:
        text = f.read()
        get_func('exec',text)
