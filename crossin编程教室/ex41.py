# -*- coding: UTF-8 -*-
import random
from urllib import urlopen  # 从指定的 URL 地址获取网页数据
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []  # 创建列表

PHRASES = {
	"class %%%(%%%):":
		"Make a class named %%% that is-a %%%.",
	"class %%%(object):\n\tdef __init__(self, ***)" :
		"class %%% has-a __init__ that takes self and *** parameters.",
	"class %%%(object):\n\tdef ***(self, @@@)":
		"class %%% has-a function named *** that takes self and @@@ parameters.",
	"*** = %%%()":
		"Set *** to an instance of class %%%.",
	"***.***(@@@)":
		"From *** get the *** function, and call it with parameters self, @@@.",
	"***.*** = '***'":
		"From *** get the *** attribute and set it to '***'."
}  # 创建字典

# do then want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":  # sys.argv[]用于程序外部传递参数，[0]是脚本名
	PHRASE_FIRST = True
else:
	PHRASE_FIRST = False

# load up the words from the website
for word in urlopen (WORD_URL).readlines():  # readlines()一次性读取整个文件，自动将文件内容分析成一个行的列表
	WORDS.append(word.strip())  # strip()用于移除字符串头尾指定的字符或字符序列，default为空格或换行符

def convert(snippet, phrase):  # 定义convert函数，参数为snippet和phrase
	class_names = [w.capitalize() for w in
				  random.sample(WORDS, snippet.count("%%%"))]
	other_names = random.sample(WORDS, snippet.count("***"))  # random.sample()从指定的序列中，随机的截取指定长度的片断，不作原地修改
	results = []
	param_names = []
	
	for i in range (0, snippet.count("@@@")):
		param_count = random.randint(1, 3)
		param_names.append(', '.join(random.sample(WORDS, param_count)))
	
	for sentence in snippet, phrase:
		result = sentence[:]
		
		# fake class names
		for word in class_names:
			result = result.replace("%%%", word, 1)
		
		#fake other names
		for word in other_names:
			result = result.replace("***", word, 1)
		
		for word in param_names:
			result = result.replace("@@@", word, 1)
		
		results.append(result)
	return results

# keep going until they hit CTRL-D
try:
	while True:
		snippets = PHRASES.keys()
		random.shuffle(snippets)
		
		for snippet in snippets:
			phrase = PHRASES[snippet]
			question, answer = convert(snippet, phrase)
		if PHRASE_FIRST:
			qiestion, answer = answer, question
		
		print question;;;
		
		raw_input('> ')
		print "ANSWER: %s\n\n" % answer
except EOFError:
	print "\nBye"

