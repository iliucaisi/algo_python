import sys

def is_valid(step, x1, x2, n):
    y1 = step - x1
    y2 = step - x2
    return True if x1 >= 0 and x1 < n and x2 >= 0 and x2 < n and y1 >= 0 and y1 < n and y2 >= 0 and y2 < n else False
def get_value(step, x1, x2, n):
    return dp[step][x1][x2] if is_valid(step, x1, x2, n) else NEG_INF
def min_path_sum(a, n):
    P = n * 2 - 2
    global dp
    dp = [[[0 for i in range(n)] for i in range(n)] for i in range(2 * n)]
    
    i = 0
    while i < n:
        j = i
        while j < n:
            dp[0][i][j] = NEG_INF
            j += 1
        i += 1
    step = 1
    dp[0][0][0] = a[0][0]
    while step <= P:
        i = 0
        while i < n:
            j = i
            while j < n:
                dp[step][i][j] = NEG_INF

                if not is_valid(step, i, j, n):
                    j += 1
                    continue
                if i != j:
                    dp[step][i][j] = max(dp[step][i][j], get_value(step - 1, i - 1, j - 1, n))
                    dp[step][i][j] = max(dp[step][i][j], get_value(step - 1, i - 1, j, n))
                    dp[step][i][j] = max(dp[step][i][j], get_value(step - 1, i, j - 1, n))
                    dp[step][i][j] += a[i][step - i] + a[j][step - j]
                else:
                    dp[step][i][j] = max(dp[step][i][j], get_value(step - 1, i - 1, j - 1, n))
                    dp[step][i][j] = max(dp[step][i][j], get_value(step - 1, i - 1, j, n))
                    dp[step][i][j] = max(dp[step][i][j], get_value(step - 1, i, j - 1, n))
                    dp[step][i][j] += a[i][step - i]
                print dp[step][i][j] 
                j += 1
            i += 1
        step += 1
    print "Final dp="
    i = 0
    while i < 2 * n:
        print dp[i]
        i += 1
    print "Maximum sum: ", dp[P][n - 1][n - 1]
    return dp[P][n - 1][n - 1]

##################################################
#                   main                         #
##################################################

NEG_INF=-sys.maxint-1
str1 = sys.argv[1].split(';')
dp = None

a = [[] for i in range(len(str1))]
i = 0
while i < len(str1):
    j = 0
    row = str1[i].split(',')
    while j < len(str1):
        a[i].append(int(row[j]))
        j += 1
    i += 1

if len(sys.argv) == 3:
    n = int(sys.argv[2])
else:
    n = len(a[0])

print "Matrix is: ", a
min_path_sum(a, n)
