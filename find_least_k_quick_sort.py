import sys

def get_pivot(digits, start, end):
    if end < start:
        return -1
    current = digits[start]
    while start < end:
        while end > start and digits[end] >= current:
            end = end - 1
        digits[start] = digits[end]
        while start < end and digits[start] < current:
            start = start + 1
        digits[end] = digits[start]
    digits[start] = current
    return start

def find_quick(digits, k):
    findings=[]
    if k <= 0:
        return findings
    len_digits = len(digits) 
    pivot = get_pivot(digits, 0, len_digits - 1)
    
    if pivot < k - 1:
        findings.extend(digits[0:pivot+1])
        findings.extend(find_quick(digits[(pivot + 1):], (k - 1 - pivot)))
    elif pivot > k - 1:
        findings.extend(find_quick(digits[:pivot], k))
    else:
        findings.extend(digits[:pivot+1])
    return findings

##################################################
#                    main                        #
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
print "Least ", k, " is: ", find_quick(digits, k)
