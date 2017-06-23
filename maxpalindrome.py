import sys

##################################################
#                    Main						 #
##################################################
str1 = sys.argv[1]
max_palindrome=''

i = 0
str1_len = len(str1)
while i < str1_len:
	step = 1
	while (i - step >= 0) and (i + step < str1_len):
		if str1[i - step] == str1[i + step]:
			step = step + 1
			continue
		break

	step = step - 1
#   	print "Odd max palindrome is: ", str1[(i - step): (i + step + 1)]
	if len(max_palindrome) < (step * 2 + 1):
		max_palindrome = str1[(i - step): (i + step + 1)]

	j = i + 1
	if j < str1_len:
		if str1[i] == str1[j]:
			step = 1
			while (i - step) >= 0 and (j + step < str1_len):
				if str1[i - step] == str1[j + step]:
					step = step + 1
					continue
				break
			
			step = step - 1
#			print "Even max palindrome is: ", str1[(i - step): (j + step + 1)]
			if len(max_palindrome) < (step * 2 + 2):
				max_palindrome = str1[(i - step): (j + step + 1)]

	i = i + 1		
print "Max palindrome is: ", max_palindrome
