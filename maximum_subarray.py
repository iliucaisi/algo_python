import sys

def max_subarray(digits):
    len_digits = len(digits)
    cur_sum = 0
    max_sum = 0
    i = 0
    while i < len_digits:
        if cur_sum < 0:
            cur_sum = digits[i]
        else:
            cur_sum = cur_sum + digits[i]

        if cur_sum > max_sum:
            max_sum = cur_sum
        
        i = i + 1
    return max_sum

##################################################
#	                main        	         	 #	
##################################################

if len(sys.argv) != 2:
	print "Usage:"
	print "\tpython ", __file__, " <array>"
	print "\t<array> separated by comma"
	exit(0)

it = iter(sys.argv[1].split(","))

digits = []
while True:
	try:
		digits.append(int(it.next()))
	except StopIteration:
		break
print "DEBUG original array: ", digits
print "Maximum subarray is: ", max_subarray(digits)

