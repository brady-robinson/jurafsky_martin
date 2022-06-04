import re

# Basic regualar expression patterns

# string_array = ["Elephant","elephants", "elephant",
# 	"elephantine", "morning"]

# for string in string_array:
# 	match = re.findall("[Ee]lephants?", string)
# 	if match:
# 		print(string)
# 	else:
# 		print("no match")


# string_array2 = ["hello1", "goodbye"]

# for string in string_array2:
# 	match = re.findall("[0-9]", string)
# 	if match:
# 		print(string)
# 	else:
# 		print("no match")

# string_array3 = ["Elephant","elephants", "elephant",
# 	"elephantine", "morning"]

# for string in string_array3:
# 	match = re.findall("[^e]", string)
# 	if match:
# 		print(string)
# 	else:
# 		print("no match")

# Disjunction, grouping, and precendence

# word_list = ["guppish", "guppy", "guppies", "gupper"]

# for word in word_list:
# 	match = re.findall("gupp(y|ies)", word)
# 	if match:
# 		print(word)
# 	else:
# 		print("no match")

# A simple example

# word_list = ["other","the fox and hen", "the2 fox and the1 hen", "The fox and the hen",
# 			"The43 fox and The43 hen"]

# for word in word_list:
# 	match = re.findall("the", word)
# 	if match:
# 		print(word)
# 	else:
# 		print("no match")

# for word in word_list:
# 	match = re.findall(r"\b[tT]he\b", word)
# 	if match:
# 		print(word)
# 	else:
# 		print("no match")

# for word in word_list:
# 	match = re.findall("(^|[^a-zA-Z])[tT]he([^a-zA-Z]|$)", word)
# 	if match:
# 		print(word)
# 	else:
# 		print("no match")

# A more complex example

# word_list = ["a PC with 5 GHz and 200 GB of disk space for $1001",
# 			"a PC with 7 GHz and 500 GB of disk space for $999"]

# for word in word_list:
# 	match = re.findall(r"$1001", word)
# 	#match = re.findall(r"\b$[0-9]+(\.[0-9][0-9])?\b", word)
# 	if match:
# 		print(word)
# 	else:
# 		print("no match")

# Use of an finite state automata (FSA) to recognize sheeptalk

# with a regex

# word_list = ['baaa!', 'bdaaa!', 'ba!', 'baa!']

# for word in word_list:
# 	match= re.findall("ba(a|a+)!", word)
# 	if match:
# 		print(word)
# 	else:
# 		print("no match")

# with a function

# tape = ["b","a","a","a", "a","a","a","!"]
# machine = {0: {"b":1, "a": "FAIL", "!": "FAIL"}, 
# 			1: {"b":"FAIL", "a": 2, "!": "FAIL"},
# 			2: {"b":"FAIL", "a": 3, "!": "FAIL"},
# 			3: {"b":"FAIL", "a": 3, "!": 4},
# 			4: {"b":"FAIL", "a": "FAIL", "!": "FAIL"}}

# def d_recognize(tape, machine):
# 	index = 0
# 	current_state = 0

# 	try:
# 		while index <= len(tape):
# 			if index == len(tape)-1:
# 				if current_state != "FAIL":
# 					return "accept"
# 				else:
# 					return "reject"
# 			elif machine[current_state][tape[index]] == "FAIL":
# 				return "reject"
# 			else:
# 				current_state = machine[current_state][tape[index]]
# 				index += 1
# 	except KeyError:
# 		return "reject"

# print(d_recognize(tape, machine))








