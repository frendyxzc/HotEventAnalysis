from flask import Flask, jsonify, render_template, request  
import chartkick
import re
import json
import sys

reload(sys);
sys.setdefaultencoding('utf-8');
  
app = Flask(__name__, static_folder=chartkick.js());
app.jinja_env.add_extension("chartkick.ext.charts");

class CCode:  
	def str(self, content, encoding='utf-8'):  
		return json.dumps(content, encoding=encoding, ensure_ascii=False, indent=4)  
		pass
	pass
 
@app.route('/')  
@app.route('/index')  
def index():
	cCode = CCode();
	
	# realtime hot
	results = file("./data/list_realtimehot.result").read();
	pattern = re.compile(r'(.+?),(.+?),(.+?);', re.S);
	datas = re.findall(pattern, results);
	
	n = 0;
	dict = {};
	for data in datas:
		list = ['' for n in range(2)];
		list[0] = data[2];
		list[1] = data[1];
		if(dict.has_key(data[0])):
			dict[data[0]].append(list);
		else:
			dict[data[0]] = [];
			dict[data[0]].append(list);
			n = n + 1;

	list = [];
	for key in dict.keys():
		dict2 = {};
		dict2["name"] = key;
		dict2["data"] = dict[key];
		list.append(dict2);
		
	# topic
	results = file("./data/list_topic.result").read();
	pattern = re.compile(r'(.+?),(.+?),(.+?),(.+?);', re.S);
	datas = re.findall(pattern, results);
	
	n = 0;
	dict = {};
	for data in datas:
		list2 = ['' for n in range(2)];
		list2[0] = data[2];
		list2[1] = data[1];
		if(dict.has_key(data[0])):
			dict[data[0]].append(list2);
		else:
			dict[data[0]] = [];
			dict[data[0]].append(list2);
			n = n + 1;

	list2 = [];
	for key in dict.keys():
		dict2 = {};
		dict2["name"] = key;
		dict2["data"] = dict[key];
		list2.append(dict2);

	return render_template('index.html', realtimehot=cCode.str(list), topic=cCode.str(list2));
  
  
if __name__ == "__main__":  
    app.run(debug=True);