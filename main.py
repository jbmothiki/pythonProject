#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusminus(arr):
    positive = negative = zero = 0
    for i in arr:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += 1
        elif i == 0:
            zero += 1
    print(f'{positive/n:.6f}')
    print(f'{negative/n:.6f}')
    print(f'{zero/n:.6f}')


if __name__ == '__main__':
    n = 6

    arr = [-4, 3, -9, 0, 4, 1]

    plusminus(arr)
