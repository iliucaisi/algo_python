import sys

def get_index(str1):
	len_str1 = len(str1)
	if len_str1 <= 0:
		return
	
	code = 0
	code = code + (to_int(str1[0]) - to_int('a')) * (3 + 25 ** 3)
	if len_str1 == 4:
		code = code + (to_int(str1[1]) - to_int('a')) * (25 ** 2)
		code = code + (to_int(str1[2]) - to_int('a')) * 25
		code = code + (to_int(str1[3]) - to_int('a')) + 1
		code = code + 3

	if len_str1 == 3:
		code = code + 3
	if len_str1 == 2:
		code = code + 2
	if len_str1 == 1:
		code = code + 1
	return code - 1

def get_code(num):
	num = int(num) 
	code = []
	i = num / (3 + 25 ** 3)
	if i >= 0:
		code.append(to_char(i + 97))
	
	j = num % (3 + 25 ** 3)

	if j > 3:
		k = (j - 3) / 25 ** 2
		code.append(to_char(k + 97))
		l = ((j - 3) % 25 ** 2) / 25
		code.append(to_char(l + 97))
		m = ((j - 3) % 25 ** 2) % 25
		code.append(to_char(m + 97))
	
	if j == 3:
		code.append('aa')
	if j == 2:
		code.append('a')
	
	return "".join(code)
	

def to_int(c):
	return ord(c)

def to_char(i):
	return chr(i)

##################################################
#					Main						 #
##################################################

if len(sys.argv) != 3:
	exit(0)

op = sys.argv[1]
arg = sys.argv[2]

if op == "get_code":
	print get_code(arg)
elif op == "get_index":
	print get_index(arg)
