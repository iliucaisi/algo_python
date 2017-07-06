import sys

def find_more_than_half_number(numbers):
    len_numbers = len(numbers) 
    if len_numbers == 0:
        return
    candidate = numbers[0]
    times = 1
    i = 1
    while i < len_numbers:
        if times == 0:
            candidate = numbers[i]
            times = 1
        else:
            if candidate == numbers[i]:
                times += 1
            else:
                times -= 1
        i += 1 
    return candidate


##################################################
#	            main	         	 #
##################################################

if len(sys.argv) != 2:
    print "Usage: "
    print "\tpython ", __file__, " <numbers>"
    print "\t<numbers> separated by comma."
    exit(0)

list_it = iter(sys.argv[1].split(','))
numbers = []
while True:
    try:
        numbers.append(int(list_it.next()))
    except StopIteration:
        break

print "More than half number is: ", find_more_than_half_number(numbers)
