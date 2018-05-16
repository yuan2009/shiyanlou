#!/usr/bin/env python3
filename = '/Users/yuanxiao/Desktop/shiyanlou/lession7/test.txt'

with open(filename) as file:
    count = 0
    for line in file:
        count += 1
        print(count)
    print("line: ", count)


