import sys
##################################################
#                    Main						 #
##################################################
str1 = sys.argv[1]

left = 0
right = len(str1) - 1

while left < right:
	if str1[left] == str1[right]:
		left = left + 1
		right = right - 1
		continue
	break

if left == right:
	print "Parlindrome yes"
else:
	print "Parlindrome no"
