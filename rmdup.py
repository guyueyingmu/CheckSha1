#!/usr/bin/python
# -*- coding: UTF-8 -*-
import csv
import os
import pathlib

def get_repeatsha1(filePath):
    g = os.walk(filePath)
    rpsha1s = {}
    for path, dir_list, file_list in g:
        for file_name in file_list:
            fullname = os.path.join(path, file_name)
            print(fullname)
            with open(fullname, 'rt', encoding='utf-8', errors='replace') as f:
                data = f.read().replace(r'115://',r'').replace('\r',"").split('\n')
                for line in data:
                    arrsha1 = line.split('|')
                    if len(arrsha1) >3:
                        rpsha1s.update({arrsha1[2]:'1'})
    return rpsha1s
def get_mysha1s(filePath):
    g = os.walk(filePath)
    mysha1s = {}
    i = 0;
    for path, dir_list, file_list in g:
        for file_name in file_list:
            fullname = os.path.join(path, file_name)
            print(fullname)
            with open(fullname, 'rt', encoding='utf-8', errors='replace') as f:
                data = f.read().replace(r'115://',r'').replace('\r',"").split('\n')
                for line in data:
                    arrsha1 = line.split('|')
                    l=len(arrsha1)
                    if l > 3:
                        size =int(arrsha1[1])
                        id ='%s|%s|%s' % (arrsha1[1] , arrsha1[2],arrsha1[3])
                        if size > 20000000 :
                            if l> 4:
                                arrsha1[0]=arrsha1[4]+'>'+ arrsha1[0]
                            sname = mysha1s.get(id)
                            if sname:
                                arrsha1[0] = arrsha1[0] + '|' + sname
                                arrsha1[0] = '|'.join({}.fromkeys(arrsha1[0] .split('|')).keys())
                            mysha1s.update({id: arrsha1[0]})

    res = ''
    resnew = ''
    rpsha1s = get_repeatsha1('RepeatSha1')
    for id in mysha1s:
        res = res + "1.c|"+id +"|" +mysha1s[id]+'\n'
        # print(id.split('|')[1])
        rp = rpsha1s.get(id.split('|')[1])
        # print(rp)
        if not rp:
            resnew = resnew +"1.n|"+id +"|" +mysha1s[id]+'\n'

    with open('AllMySha1.txt', 'w' ,encoding='utf-8') as f:
        f.write(res)
    if resnew == '':
        print('没有发现符合条件的新sha1')
    else:
        with open('NewSha1.txt', 'w' ,encoding='utf-8') as f:
            f.write(resnew)

get_mysha1s("MySha1")
quit()