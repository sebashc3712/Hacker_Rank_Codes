#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):

    count_a=0
    length_s=len(s)

    if n<length_s:

        for i in range(0,n):

            if s[i]=="a":

                count_a+=1
        
        return count_a

    else:

        for i in range(0,length_s):

            if s[i]=="a":

                count_a+=1
        
        if n%length_s==0:

            return int((n/length_s)*count_a)
        
        else:

            temp=int(math.floor(n/length_s)*count_a)
            steps=(((n/length_s)-math.floor(n/length_s))*length_s)

            frac,temp2=math.modf(steps)

            if frac<0.01:

                steps=math.floor(steps)

            else:

                steps=math.ceil(steps)

            new_count_a=0

            for i in range(0,steps):

                if s[i]=="a":

                    new_count_a+=1
            
            return temp+new_count_a

        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
