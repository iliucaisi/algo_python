import sys

def compress_and_reverse(str1):
	str1_len = len(str1)
	i = 0
	start = -1
	compressed_and_reversed = []
	skip = False
	while i < str1_len:
		if str1[i] == ' ' and skip == False:
			if start != -1:
				compressed_and_reversed.append(str1[start:i][::-1])
			skip = True
		if skip == True and str1[i] != ' ':
			start = i
			skip = False
		i = i + 1
	if skip == False:
		compressed_and_reversed.append(str1[start:i][::-1])

	return " ".join(compressed_and_reversed)

##################################################
#				Main							 #
##################################################

str1 = sys.argv[1]
print compress_and_reverse(str1)

