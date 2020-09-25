#!/usr/bin/env python
# coding=utf-8

import requests
from bs4 import BeautifulSoup
from re_test import *

class Searcher():
    def __init__(self,args):
        try:
            self.func_name = args[0]
            self.offset = args[1]
        except:
            return
    text = ''
    def parser_html(self,text):
            cout = 0
            l = []
            soup = BeautifulSoup(text,'html.parser')
            for i in soup.find_all('a'):
                if i.get('class')==[u'lib-item']:
                    libc = i.text.split()
                    l.append(libc[0])
                    cout += 1
            if cout == 0:
                return None,0
            print l
            return l,cout
    @staticmethod
    def equip_url(libc,url):
        url = 'https://publicki.top/d/'
        url += libc + '.symbols'
        print url
        r = requests.get(url)
        if r.status_code==200:
            return r.text
        else:
            print 'get libc information error'
            return None
       
    def searcher(self):
        func_name = self.func_name
        offset = self.offset
        url = 'https://publicki.top/libc/?q='
        url += func_name
        url += '%3A'
        url += hex(offset)
        r=requests.get(url)
        global text
        base_addr = 0
        if r.status_code == 200:
           ret,cout =  self.parser_html(r.text)
           if cout==0:
               print 'not found'
               return None
           elif cout>1:
               number = input('select a database:\n')
               while number>cout-1  or number<0:
                   number = input('please choose again:\n')
               ret[0] = ret[number]
           text = self.equip_url(ret[0],url)
           base_addr = offset-get_func(func_name,text)
           return base_addr
        else:
            print r.status_code
            return None

if __name__ == "__main__":
    test = Searcher(('__libc_start_main_ret',0xe81))
    print test.searcher()
