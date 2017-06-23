#! /usr/bin/env python
# encoding: utf-8
import matplotlib.pyplot as plt
import jieba
import sys
import numpy as nm

reload(sys)
sys.setdefaultencoding('utf-8')
# part 1:情感词典录入
positive_emotion = []
negative_emotion = []
extreme = []
very = []
more = []
alittlebit = []
insufficiently = []
over = []
no = []
d = open("positive-emotion.txt")
d2 = open("positive_evaluate.txt")
n = open("negative-emotion.txt")
n22 = open("negative_evaluate.txt")
e = open("extreme-6.txt")
v = open("very-5.txt")
m = open("more-4.txt")
a = open("alittlebit-3.txt")
i = open("insufficiently-2.txt")
o = open("over-1.txt")
n2 = open("no.txt")
for line in d.readlines():
    positive_emotion.append(line.strip())
for line in d2.readlines():
    positive_emotion.append(line.strip())
for line in n.readlines():
    negative_emotion.append(line.strip())
for line in n22.readlines():
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
    no.append(line.strip().encode('utf-8'))

# 句子情感的识别与分析
# input =open(input.txt)

# for line in open("out.txt").readlines():
line = raw_input()
aline = jieba.cut(line, cut_all=False)
emotions = []
emotion_value = 0
not_num = 0
emotion_times = 1
for word in aline:
    #print(word)
    if word in positive_emotion:
        emotion_value = 2 * ((-1) ** not_num) * emotion_times
        emotions.append(emotion_value)
        not_num = 0
        emotion_times = 1
        # positive
    elif word in negative_emotion:
        not_num = not_num + 1
        emotion_value = 2 * ((-1) ** not_num) * emotion_times
        emotions.append(emotion_value)
        not_num = 0
        emotion_times = 1
        # negative
    elif word in extreme:
        emotion_times = emotion_times + 2
    elif word in very:
        emotion_times = emotion_times + 1.4
    elif word in more:
        emotion_times = emotion_times + 1
    elif word in alittlebit:
        emotion_times = emotion_times + 0.4
    elif word in insufficiently:
        emotion_times = emotion_times - 0.2
    elif word in over:
        emotion_times = emotion_times + 1.2
    elif word in no:
        not_num += 1
    elif word == "！":
        if emotions[len(emotions)-1] > 0:
            emotions[len(emotions)-1]+=1
        else:
            emotions[len(emotions)-1]-=1

print '情感均值：'+str(sum(emotions)/len(emotions))
print '情感方差：'+str(nm.cov(emotions))
x1=range(0,len(emotions))
plt.plot(x1,emotions,label='emotion values',marker='.',markerfacecolor='red',markersize=12)
plt.xlabel('emotion_words_apper_times')
plt.ylabel('emotion_value')
plt.legend()
plt.ylim(-10,10)
plt.show()