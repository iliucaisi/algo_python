import sys

def adjust(digits, start, end):
    if start > end:
        return

    while start >= 0:
        left = start * 2 + 1
        right = start * 2 + 2
        max_child = left
        if right <= end and left <= end and digits[right] < digits[left]:
            max_child = right
        if max_child <= end and digits[max_child] < digits[start]:
            digits[start], digits[max_child] = digits[max_child], digits[start]
        if start == 0:
            break
        start = start / 2

def create_heap(digits):
    len_digits = len(digits)

    i = (len_digits - 1) / 2
    while i > 0:
        adjust(digits, i, len_digits - 1)
        i = i - 1

def find(digits, k):
    len_digits = len(digits)	
    
    end = (len_digits - 1) / 2
    finding = []
    while k > 0 and end >= 0:
        finding.append(digits[0])
        digits[0], digits[end] = digits[end], digits[0]
        end = end - 1
        i = end / 2
        while i > 0:
            adjust(digits, i, end)
            i = i - 1
        k = k - 1
    
    return finding     
	
##################################################
#	            main	         	 #	
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
print "DEBUG original digits: ", digits
create_heap(digits)
print "DEBUG heap digits: ", digits
print "Least ", k, " is: ", find(digits, k)

