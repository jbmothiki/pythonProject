#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def time_conversion(s):
    hours = int(s[:2].replace('12', '00'))
    if s[-2:] == 'PM':
        return str(hours + 12) + s[2:-2]
    return f'{hours:02d}' + s[2:-2]


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = '12:01:00PM'

    result = time_conversion(s)

    # fptr.write(result + '\n')

    # fptr.close()

    print(result)
