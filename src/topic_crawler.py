#!/usr/bin/python
import os
import sys
import re
import subprocess
import time
import datetime
import random

ISOTIMEFORMAT = "%Y%m%d%H%M%S";
TOPIC_ADDR = "http://d.weibo.com/100803?from=unlogin";
TEMP_FILE_NAME = "./data/list_topic_";
RESULT_FILE_NAME = "./data/list_topic.result";

FREE_PROXY = ['121.196.202.46:8118', '112.228.35.24:8888', '111.225.232.85:8118',
				'120.25.105.45:81', '110.154.44.80:8888', '218.106.205.145:8080',
				'122.228.179.178:80', '122.5.227.57:8888', '115.159.185.186:8088',
				'118.180.15.151:8102', '122.72.32.73:80', '124.88.67.63:80',
				'60.194.100.51:80', '101.53.101.172:9999', '60.191.239.236:80',
				'139.196.108.68:80', '115.159.237.85:808', '1.60.14.225:8888'];

def getDom(url):
	index = random.randint(0, len(FREE_PROXY)) % len(FREE_PROXY);
	cmd='./../phantomjs-2.1.1/bin/phantomjs /js/body_topic.js "%s"'%url
	#cmd='./../phantomjs-2.1.1/bin/phantomjs --proxy=' + FREE_PROXY[index] + ' /js/body_topic.js "%s"'%url
	print "cmd:", cmd
	stdout,stderr = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate();
	if stderr.strip() != '':
		print stderr;
	return stdout;


if __name__=="__main__":
	stamp = datetime.datetime.fromtimestamp(int(time.time())).strftime(ISOTIMEFORMAT);

	content = getDom(TOPIC_ADDR);
	#content = getDom(sys.argv[1]);
	
	#f=file(TEMP_FILE_NAME + stamp + ".data", "w+");
	#f.writelines(content);
	#f.close();
	#print "** finish to write file **"
	
	pattern_key = re.compile(r'<img src=".*?" alt="#(.+?)#".*?<span class="number">(.+?) </span>', re.S);
	keys = re.findall(pattern_key, content);
	
	f=file(RESULT_FILE_NAME,"a");
	for index in range(len(keys)):
		key = keys[index];
		tmp = key[0] + "," + key[1] + "," + stamp + "," + bytes(index) + ";";
		f.writelines(tmp);
	f.close();
	print "** finish to print results **"