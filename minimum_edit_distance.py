import sys

def edit_distance(src, dest):
    len_src = len(src)
    len_dest = len(dest)

    dp = [[] for i in range(len_src)]
    dp[0].append(0)
    i = 1
    while i < len_src:
        dp[i].append(i)
        i += 1
    j = 1
    while j < len_dest:
        dp[0].append(j)
        j += 1
    i = 1    
    while i < len_src:
        j = 1
        while j < len_dest:
            if src[i] == dest[j]:
                dp[i].append(dp[i - 1][j - 1])
            else:
                dp[i].append(1 + min(dp[i - 1][j], dp[i][j - 1]))
            j += 1
        i += 1
    print dp
        
    return dp[len_src - 1][len_dest - 1]


##################################################
#                   main                         #
##################################################

if len(sys.argv) != 3:
    print "Usage:"
    print "\tpython ", __file__, " <src>", " <dest>"
    print "<src>,<dest> are strings"
    exit(0)

src = sys.argv[1]
dest = sys.argv[2]

print "The distance to edit ", src, " to ", dest, " is: ", edit_distance(src, dest)


