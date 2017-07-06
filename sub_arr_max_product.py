import sys

def brute_search(numbers):
    len_numbers = len(numbers)

    i = 0
    max_product = sys.float_info.min
    while i < len_numbers:
        j = i
        while j < len_numbers:
            k = i
            cur_product = 1
            while k <= j:
                cur_product *= numbers[k]
                k += 1
            if cur_product > max_product:
                max_product = cur_product
            j += 1
        i += 1
    
    return max_product

def dynamic_search(numbers):
    len_numbers = len(numbers)
    maxend = numbers[0]
    minend = numbers[0]
    max_product = numbers[0]
    i = 1
    while i < len_numbers:
        end1 = maxend * numbers[i]
        end2 = minend * numbers[i]

        maxend = max(max(end1, end2), numbers[i])
        minend = min(min(end1, end2), numbers[i])

        max_product = max(max_product, maxend)

        i += 1
#   why can not return maxend        
#    return maxend
    return max_product


##################################################
#                   main                         #
##################################################

if len(sys.argv) != 2:
    print "Usage:"
    print "\tpython ", __file__, " <number_array>"
    print "<number_array> separated by comma."
    exit(0)

list_it = iter(sys.argv[1].split(','))
numbers = []
while True:
    try:
        numbers.append(float(list_it.next()))
    except StopIteration:
        break
# print "Max product sub array: ", brute_search(numbers)
print "Max product sub array: ", dynamic_search(numbers)

