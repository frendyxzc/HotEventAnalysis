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

results = file("./data/list_topic.result").read();

pattern = re.compile(r'(.+?),(.+?),(.+?),(.+?);', re.S);
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

list = [['' for col in range(h+1)] for row in range(k*2+2)];
list[0][0] = '';
i = 1;
j = 1;
for index in range(k*2):
	if index == k:
		i = i + 1;
	list[i][0] = key_name[index%k];
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
	list[x][y] = data[3];
	
	num = re.findall(r'\d+',data[1]);
	tmp = num[0];
	if '亿' in data[1]:
		tmp = bytes(num[0]) + '0000';
	list[x+k+1][y] = tmp;


with open('./result/result_topic.csv', 'wb') as csvfile:
	csvfile.write(codecs.BOM_UTF8);
	spamwriter = csv.writer(csvfile, dialect='excel');
	spamwriter.writerows(list);