import sys

def find(digits, k):
	len_digits = len(digits)
	if k <=0 and len_digits <=0:
		return None
        if len_digits <=k:
            print "least k elment: ", digits[0: k] 
            return 

	i = 0
	k_max = 0
	while i < k:
		if digits[k_max] < digits[i]:
			k_max = i
		i = i + 1

	while i < len_digits:
		if digits[i] < digits[k_max]:
			digits[k_max], digits[i] = digits[i], digits[k_max]
			j = 0
			while j < k:
				if digits[k_max] < digits[j]:
					k_max = j
				j = j + 1
		i = i + 1
			
	print "least k elment: ", digits[0: k] 


##################################################
#			main			 #
##################################################

if len(sys.argv) != 3:
	print "Usage:"
	print "\tpython ", __file__, " <str1> <k>"
	print "\t<str1> separated by comma"
	exit(0)

it = iter(sys.argv[1].split(","))

digits = []
while True:
	try:
		digits.append(int(it.next()))
	except StopIteration:
		break
k = int(sys.argv[2])
find(digits, k) 
