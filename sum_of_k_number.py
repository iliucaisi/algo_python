import sys

def sum_k_number(num, k):
    if k <= 0 or num <= 0:
        return

    if num == k:
        k_number.append(k)
        print "INFO k number: ", k_number
        k_number.pop()
        
    
    k_number.append(k)
    sum_k_number(num - k, k - 1) 
    k_number.pop()
    sum_k_number(num, k - 1)

##################################################
#                   main                         #
##################################################
num = int(sys.argv[1])
k = int(sys.argv[2])
k_number = []

sum_k_number(num, k)
