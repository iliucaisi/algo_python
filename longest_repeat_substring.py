import sys

def brute(str1):
	len_str1 = len(str1)

	if len_str1 <= 0:
		return
	
	longest = 0
	start1 = -1
	start2 = -1
	i = 0
	while i < len_str1:
		j = i + 1
		while j < len_str1:
			m = i
			n = j
			length = 0
			while m < len_str1 and n < len_str1 and str1[m] == str1[n]:
				m = m + 1
				n = n + 1
				length = length + 1
			if longest < length:
				longest = length
				start1 = i
				start2 = j
		
			j = j + 1
		i = i + 1
	
	print "start1=", start1, "start2=", start2, "length=", longest

def dynamic_programming(str1):
	len_str1 = len(str1)

	# Initialiaze weight table
	
	weight = [[0 for i in range(len_str1)] for i in range(len_str1)]
	
	i = 0
	j = 1
	while j < len_str1:
		if str1[0] == str1[j]:
			weight[0][j] = 1
		j = j + 1

	i = 1
	while i < len_str1:
		if str1[i] == str1[0]:
			weight[i][0] = 1
		j = 1
		while j < len_str1:
			if i !=j and str1[i] == str1[j]:
				weight[i][j] = weight[i - 1][j - 1] + 1
			j = j + 1
		i = i + 1
	
	i = 0
	longest = 0
	start1 = -1
	start2 = -1
	while i < len_str1:
		j = 0
		while j < len_str1:
			if longest < weight[i][j]:
				longest = weight[i][j]
				start1 = i - longest + 1
				start2 = j - longest + 1	
			j = j + 1
		i = i + 1
	
	print "start1=", start1, "start2=", start2, "length=", longest
##################################################
#                     main					  	 #     
##################################################

op = sys.argv[1]
str1 = sys.argv[2]

if op == "brute": 
	brute(str1)
elif op == "dynamic_programming":
	dynamic_programming(str1)
