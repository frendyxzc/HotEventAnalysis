#!/usr/bin/python
import os
import sys
import re
import subprocess
import time
import datetime

ISOTIMEFORMAT = "%Y%m%d%H%M%S";
REALTIME_HOT_ADDR = "http://s.weibo.com/top/summary?cate=realtimehot";

def getDom(url):
	cmd='./../phantomjs-2.1.1/bin/phantomjs /js/body.js "%s"'%url
	#print "cmd:", cmd
	stdout,stderr = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate();
	if stderr.strip() != '':
		print stderr;
	return stdout;


if __name__=="__main__":
	stamp = datetime.datetime.fromtimestamp(int(time.time())).strftime(ISOTIMEFORMAT);

	content = getDom(REALTIME_HOT_ADDR);
	#content = getDom(sys.argv[1]);
	
	f=file("./data/list_realtimehot_" + stamp + ".data", "w+");
	f.writelines(content);
	f.close();
	print "** finish to write file **"
	
	pattern_key = re.compile(r'<a href="/weibo/.*?Refer=top" target="_blank" suda-data="key=tblog_search_list&amp;value=list_realtimehot">(.+?)</a>.*?<p class="star_num"><span>(.+?)</span></p>', re.S);
	keys = re.findall(pattern_key, content);
	
	f=file("./data/list_realtimehot.result","a");
	for key in keys:
		tmp = key[0] + "," + key[1] + "," + stamp + ";";
		f.writelines(tmp);
	f.close();
	print "** finish to print results **"