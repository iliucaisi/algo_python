import sys

def compress(str1):
	str1_len = len(str1)
	if str1_len <= 0:
		return ""
	current = str1[0]
	i = 0
	count = 0
	compressed = []
	while i < str1_len:
		if current == str1[i]:
			count = count + 1
		else:
			compressed.append(str(count))
			compressed.append(current)
			count = 1 
			current = str1[i]
		i = i + 1
	compressed.append(str(count))
	compressed.append(current)

	return "".join(compressed)

##################################################
#				Main							 #
##################################################

str1 = sys.argv[1]
print compress(str1)


