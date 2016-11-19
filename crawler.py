#!/usr/bin/python
import os
import time
import datetime
import random

ISOTIMEFORMAT = "%Y.%m.%d-%H:%M:%S";

while (1):
	stamp = datetime.datetime.fromtimestamp(int(time.time())).strftime(ISOTIMEFORMAT);
	print stamp + ": crawler start";
	os.system("python src/realtimehot_crawler.py");
	stamp = datetime.datetime.fromtimestamp(int(time.time())).strftime(ISOTIMEFORMAT);
	print stamp + ": crawler finished\n";
	index = random.randint(10, 20);
	time.sleep(53 * index);