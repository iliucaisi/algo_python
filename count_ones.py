# coding=UTF-8
import sys

def count(start, end):
    ones = 0
    for i in range(start, end):
        ones += count_single(i)
    return ones

def count_single(num):
    if num is 0:
        return 0
    if num % 10 is 1: 
        return count_single(int(num / 10)) + 1
    else:
        return count_single(int(num / 10))

while True:
    start, end = map(int, input().split())
    if start is 0 and end is 0:
        exit(0)
    print(count(start, end + 1))


