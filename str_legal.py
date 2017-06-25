from __future__ import print_function
import sys

def find_best(n, i, m):
	if i >= m:
		print(best, '', end='')
		return
	
	j = 1
	while j <= n:
		if i == 0:
			best[i] = chr(j + 96)
			find_best(n, i + 1, m)
			j = j + 1
			continue
		if 2 * j <= n and i < m - 1:
			temp_seq_num = 2 * seq_num(best[i - 1])
			if temp_seq_num > n or temp_seq_num <= j:
				best[i] = chr(j + 96)
				find_best(n, i + 1, m)
					
		if 2 * j > n:
			best[i] = chr(j + 96)
			find_best(n, i + 1, m)
		j = j + 1	

def seq_num(c):
	return ord(c) - 96

##################################################
#					Main						 #
##################################################

n = int(sys.argv[1])
m = int(sys.argv[2])
i = 0
best = []
while i < m:
	best.append(None)
	i = i + 1


find_best(n, 0, m)
