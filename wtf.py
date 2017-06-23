#! /usr/bin/env python
#encoding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
no_word=[]
n2 =open("no.txt")
for line in n2.readlines():
    no_word.append(line.strip())
    print line.strip()
word='不'
for ano in no_word:
    if word == ano:
        print ('1')
    else:
        print(word)
        print(ano)
        print ('0')
