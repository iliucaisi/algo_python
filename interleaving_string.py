import sys

def brute(str1, str2, str3):
    len_str1 = len(str1)
    len_str2 = len(str2)
    len_str3 = len(str3)

    if len_str1 + len_str2 != len_str3:
        print "ERROR[1] len_str1=", len_str1, " len_str2=", len_str2, " len_str3=", len_str3
        return False
   
    i_str1 = 0
    i_str2 = 0
    i_str3 = 0
    while i_str1 < len_str1 and i_str2 < len_str2: 
        if str1[i_str1] == str3[i_str3]:
            if str1[i_str1] == str2[i_str2]:
                print "INFO[1] i_str1=", i_str1, " i_str2=", i_str2, " i_str3=", i_str3
                return brute(str1[i_str1 + 1:], str2[i_str2:], str3[i_str3 + 1:]) or brute(str1[i_str1:], str2[i_str2 + 1:], str3[i_str3 + 1:]) 
            else:
                i_str1 += 1
                i_str3 += 1
        elif str2[i_str2] == str3[i_str3]:
            i_str2 += 1
            i_str3 += 1
        else:
            break

    while i_str1 < len_str1: 
        if str1[i_str1] == str3[i_str3]:
            i_str1 += 1
            i_str3 += 1
        else:
            break
    
    if i_str1 != len_str1:
        print "ERROR[2] len_str1=", len_str1, " len_str2=", len_str2, " len_str3=", len_str3
        return False

    while i_str2 < len_str2: 
        if str2[i_str2] == str3[i_str3]:
            i_str2 += 1
            i_str3 += 1
        else:
            break

    if i_str2 != len_str2:
        print "ERROR[3] len_str1=", len_str1, " len_str2=", len_str2, " len_str3=", len_str3
        return False

    return True

def dynamic(str1, str2, str3):
    len_str1 = len(str1)
    len_str2 = len(str2)
    len_str3 = len(str3)

    if len_str1 + len_str2 != len_str3:
        return False
    dp = [[] for i in range(len_str1 + 1)]
    i = 0
    while i <= len_str1:
        j = 0
        while j <= len_str2:
            dp[i].append(False)
            j += 1
        i += 1
    dp[0][0] = True

    i = 0
    while i <= len_str1:
        j = 0
        while j <= len_str2:
            print "DEBUG[1]"
            if dp[i][j] is True:
                dp[i][j] = True
            elif i - 1 >= 0 and str1[i - 1] == str3[i + j -1] and dp[i - 1][j] is True:
                dp[i][j] = True
            elif j - 1 >= 0 and str2[j - 1] == str3[i + j - 1] and dp[i][j - 1] is True:
                dp[i][j] = True
            else:
                print "DEBUG[2]"
                dp[i][j] = False
            j += 1
        i += 1
    print "Final dp:", dp
    return dp[len_str1][len_str2]

##################################################
#                       main                     #
##################################################

if len(sys.argv) != 4:
    print "Usage:"
    print "\tpython ", __file__, " <str1> <str2> <str3>"
    print "<str3> is made up of <str1> and <str2>"
    exit(0)


str1 = sys.argv[1]
str2 = sys.argv[2]
str3 = sys.argv[3]

# print brute(str1, str2, str3)
print dynamic(str1, str2, str3)
