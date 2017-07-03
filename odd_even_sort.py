import sys

def is_odd(digit):
    if digit % 2 == 1:
        return True
    return False

def odd_even_sort(digits):
   len_digits = len(digits)
   i = 0
   j = len_digits - 1
   pivot_value = digits[0]
   while i < j:
       print "DEBUG i=",i,"j=",j
       while j > i and not is_odd(digits[j]):
           j = j - 1
       digits[i] = digits[j]
       while i < j and is_odd(digits[i]):
           i = i + 1
       digits[j] = digits[i]
   
   digits[i] = pivot_value
   return digits

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
print "Sorted array is: ", odd_even_sort(digits)

