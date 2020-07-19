#!/usr/bin/env python
# coding=utf-8
import requests
from bs4 import BeautifulSoup
import parser

def parser(text):
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

def get_dict(text):
    soup = BeautifulSoup(text,'html.parser')
    td = soup.find_all('td')
    x,y = 1,2
    cout = len(td)/4
    dict = {}
    for i in range(cout):
        name = td[x].text
        offset = td[y].text
        x += 4
        y += 4
        dict[name]=offset
    return dict

def equip_url(libc,url):
    url+='&l='
    url+=libc
    print url
    r = requests.get(url)
    if r.status_code==200:
        # test func 
        return r.text
    else:
        print 'get libc information error'
        return None

def searcher(func_name,offset):
    url = 'https://publicki.top/libc/?q='
    url += func_name
    url += '%3A'
    url += hex(offset)
    r=requests.get(url)
    if r.status_code == 200:
       ret,cout =  parser(r.text)
       print ret
       if cout==0:
           print 'not found'
           return None
       elif cout==1:
           # select the only database
           # equip the offsets in a dict and return
           text = equip_url(ret[0],url)
           return get_dict(text)
       else:
           # choose one database
           number = input('select a database:\n')
           text = equip_url(ret[number],url)
           if text == None:
                print 'some thing wrong here'
                return 
           return  get_dict(text)
    else :
        print r.status_code

print searcher('puts',0x9c0)
