from __future__ import print_function
import sys

def combine(m, k):
	for i in range(m, k - 1, -1):
		combined[k]=alphabet[i]
		if(k > 1):
			combine(i - 1, k - 1)
		else:
			for j in range(K_SUB, 0, -1):
				print(combined[j], end='')
			print(' ')
###################
#     main        #
###################

SET_SIZE=int(sys.argv[1])
K_SUB=int(sys.argv[2])

alphabet=[]
alphabet.append(K_SUB)
for i in range(1, 27):
	alphabet.append(chr(96 + i))

combined=[]
for i in range(0, K_SUB + 1):
	combined.append(0)

combine(SET_SIZE, K_SUB)




