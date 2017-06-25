import sys

def equipartition(str1):
	len_str1 = len(str1)
	if len_str1 <= 0 or len_str1 % 2 != 0:
		return
	
	left_start = 0
	left_end = len_str1 / 2 - 1
	left_zero_count = 0
	right_zero_count = 0
	
	i = 0 
	while i < len_str1:
		if i <= left_end:
			if str1[i] == '0':
				left_zero_count = left_zero_count + 1
		else:
			if str1[i] == '0':
				right_zero_count = right_zero_count + 1
		i = i + 1
	
	while left_zero_count != right_zero_count and left_end < len_str1 - 1:
		left_end = left_end + 1
		if str1[left_end] == '0':
			left_zero_count = left_zero_count + 1
			right_zero_count = right_zero_count - 1
		if str1[left_start] == '0':
			left_zero_count = left_zero_count - 1
			right_zero_count = right_zero_count + 1
		left_start = left_start + 1

	print "Equipartition:"
	print "Part 1: <", left_start, ",", left_end, ">"
	print "Part 2: <", left_end + 1, ",", left_start - 1, ">"
		

##################################################
# 					Main						 #
##################################################

if len(sys.argv) != 2:
	exit(0)

str1 = list(sys.argv[1])

equipartition(str1)
