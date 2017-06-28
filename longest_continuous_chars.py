import sys

def find_longest_continuous_chars(str1):
	len_str1 = len(str1)
	if len_str1 <= 0:
		return
	longest = 0
	current = -1
	count = 0

	i = 0 
	while i < len_str1:
		if current == -1:
			current = i
			longest = 1
			count = 1
		if i > 0 and str1[i - 1] == str1[i]:
			count = count + 1
		elif i > 0:
			if count > longest:
				longest = count
				current = i - longest
				count = 1
		
		i = i + 1
		
	if count > longest:
		longest = count
		current = i - longest
	
	print "Position: ", current, ",Length: ", longest


##################################################
#					main 						 #
##################################################

str1 = sys.argv[1]

find_longest_continuous_chars(str1)
