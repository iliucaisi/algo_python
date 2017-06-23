from __future__ import print_function
import sys

def charToInt(c):
	return ord(c) - 48

##################################################
#				Main							 #
##################################################			
# Did not consider int overflow.				 #
##################################################
str1 = sys.argv[1]
n = 0
sign = None
if str1[0] == '+' or str1[0] == '-':
	sign = str1[0]
	i = 1
else:
	i = 0

while i < len(str1):
	temp = charToInt(str1[i])
	if temp < 0 or temp > 9:
		print("Error illegal digit")
		break
	n = n * 10 + temp
	i = i + 1

if sign == None:
	print("Int value is: ", n)
else:
	print("Int value is: ", sign, n)
