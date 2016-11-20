#!/usr/bin/python
import os
import time
import datetime
import random
import sys

ISOTIMEFORMAT = "%Y.%m.%d-%H:%M:%S";

while (1):
	stamp = datetime.datetime.fromtimestamp(int(time.time())).strftime(ISOTIMEFORMAT);
	print stamp + ": crawler realtimehot start";
	os.system("python src/realtimehot_crawler.py");
	
	stamp = datetime.datetime.fromtimestamp(int(time.time())).strftime(ISOTIMEFORMAT);
	print stamp + ": crawler topic start";
	os.system("python src/topic_crawler.py");
	
	stamp = datetime.datetime.fromtimestamp(int(time.time())).strftime(ISOTIMEFORMAT);
	print stamp + ": crawler finished\n";
	
	index = random.randint(10, 20);
	time.sleep(53 * index);