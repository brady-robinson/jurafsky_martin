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

word_list = ["a PC with 5 GHz and 200 GB of disk space for $1001",
			"a PC with 7 GHz and 500 GB of disk space for $999"]

for word in word_list:
	match = re.findall(r"$1001", word)
	#match = re.findall(r"\b$[0-9]+(\.[0-9][0-9])?\b", word)
	if match:
		print(word)
	else:
		print("no match")




