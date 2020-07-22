#!/usr/bin/env python
# coding=utf-8
import requests
from bs4 import BeautifulSoup

global_dic = {}
global_basic_func_name = ''
global_basic_func_offset =0
global_base_addr = 0

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
    global global_dic
    for i in range(cout):
        name = td[x].text
        offset = td[y].text
        x += 4
        y += 4
        global_dic[name]=int(offset,base=16)
    return global_dic

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
    global global_basic_func_offset
    global global_basic_func_name
    global global_dic

    global_basic_func_name = func_name
    global_basic_func_offset = offset
    url = 'https://publicki.top/libc/?q='
    url += func_name
    url += '%3A'
    url += hex(offset)
    r=requests.get(url)
    if r.status_code == 200:
       ret,cout =  parser(r.text)
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
           while number>cout-1:
               number = input('please choose again:\n')
           text = equip_url(ret[number],url)
           if text == None:
                print 'some thing wrong here'
                return 
           global_dic = get_dict(text)
           return global_dic
    else :
        print r.status_code

def find(func_to_find):
    global global_base_addr
   #   print 'global dic'
   #   print global_dic
   #   print 'global offset' + str(hex(global_basic_func_offset))
   #   print 'global func name ' + str(global_basic_func_name)
    if global_base_addr == 0 and global_basic_func_offset!=0 and global_basic_func_name!='':
        global_base_addr = global_basic_func_offset-global_dic[global_basic_func_name]
        print 'global_base_addr '+ str(hex(global_base_addr))
        return find(func_to_find)
    elif global_base_addr!=0 and global_dic!={}:
        return global_dic[func_to_find]+global_base_addr
    else:
        print 'error'
        return None
