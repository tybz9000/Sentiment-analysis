#! /usr/bin/env python
#encoding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#part 1:情感词典录入
positive_emotion = []
negative_emotion=[]
extreme=[]
very=[]
more=[]
alittlebit=[]
insufficiently=[]
over=[]
no = []
d = open("positive-emotion.txt")
n= open("negative-emotion.txt")
e= open("extreme-6.txt")
v= open("very-5.txt")
m= open("more-4.txt")
a= open("alittlebit-3.txt")
i= open("insufficiently-2.txt")
o= open("over-1.txt")
n2 =open("no.txt")
for line in d.readlines():
    positive_emotion.append(line.strip())
for line in n.readlines():
    negative_emotion.append(line.strip())
for line in e.readlines():
    extreme.append(line.strip())

for line in v.readlines():
    very.append(line.strip())
for line in m.readlines():
    more.append(line.strip())
for line in a.readlines():
    alittlebit.append(line.strip())
for line in i.readlines():
    insufficiently.append(line.strip())
for line in o.readlines():
    over.append(line.strip())
for line in n2.readlines():
    no.append(line.strip())
#句子情感的识别与分析
#input =open(input.txt)
while(True):
    #for line in open("out.txt").readlines():
            line=raw_input()
            aline = line.split(",")
            emotion_value = 0
            not_num = 0
            emotion_times = 1
            for word in aline:
                if word in positive_emotion:
                    emotion_value = emotion_value + 1 * ((-1) ** not_num) * emotion_times
                    not_num = 0
                    emotion_times = 1
                #positive
                elif word in negative_emotion:
                    not_num = not_num + 1
                    emotion_value = emotion_value + 1 * ((-1) ** not_num) * emotion_times
                    not_num = 0
                    emotion_times = 1
                #negative
                elif word in extreme:
                    emotion_times = emotion_times + 3
                elif word in very:
                    emotion_times = emotion_times + 2.5
                elif word in more:
                    emotion_times = emotion_times + 2
                elif word in alittlebit:
                    emotion_times = emotion_times + 1
                elif word in insufficiently:
                    emotion_times = emotion_times - 0.5
                elif word in over:
                    emotion_times = emotion_times - 1
                elif word == "！":
                    if emotion_value>0:
                        emotion_value=emotion_value+2
                    else:
                        emotion_value=emotion_value-2
                elif word in no:
                    not_num = not_num + 1
                else:
                    continue
            print emotion_value

