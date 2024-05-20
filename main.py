import math
import os
import random
import re
import sys


#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY ary as parameter.
#

def minimax_sum(ary):
    arr_sum = 0
    min_val, max_val = ary[0], ary[0]
    for num in ary:
        arr_sum += num
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num
    print(arr_sum - max_val, arr_sum - min_val)


if __name__ == '__main__':
    arr = [1, 3, 5, 7, 9]

    minimax_sum(arr)
