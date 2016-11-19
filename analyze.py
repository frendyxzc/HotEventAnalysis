#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
import time
import datetime
import sys
import re
import csv
import codecs

def mySort(s):
    d = sorted(s,key=lambda s:s[2],reverse=False);
    return d;

results = file("./data/list_realtimehot.result").read();

pattern = re.compile(r'(.+?),(.+?),(.+?);', re.S);
datas = re.findall(pattern, results);
	
datas = mySort(datas);

# make result list
k = 0;
h = 0;
key_name = ['' for n in range(len(datas))];
key_time = ['' for n in range(len(datas))];
for data in datas:
	if data[0] not in key_name:
		key_name[k] = data[0];
		k = k + 1;
	if data[2] not in key_time:
		key_time[h] = data[2];
		h = h + 1;

list = [['' for col in range(h+1)] for row in range(k+1)];
list[0][0] = '';
i = 1;
j = 1;
for index in range(k):
	list[i][0] = key_name[index];
	i = i + 1;
for index in range(h):
	list[0][j] = key_time[index];
	j = j + 1;

for data in datas:	
	x = 0;
	y = 0;
	for index in range(len(key_name)):
		if data[0] == key_name[index]:
			x = index + 1;
	for index in range(len(key_time)):
		if data[2] == key_time[index]:
			y = index + 1;
	list[x][y] = data[1];

with open('./result/result.csv', 'wb') as csvfile:
	csvfile.write(codecs.BOM_UTF8);
	spamwriter = csv.writer(csvfile, dialect='excel');
	spamwriter.writerows(list);