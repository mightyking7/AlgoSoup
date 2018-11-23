
import sys
import re
from LCS import lcsLength, constructLCS

'''
Purpose:
   Driver for algorithm that computes the longest common subsequence

'''

def main():

    # Test cases

    fileName = sys.argv[1]

    file = open(fileName, 'r')

    test = re.compile(r'A:\s+([a-zA-Z]+),\s+B:\s+([a-zA-Z]+)')

    while True:

        line = file.readline()

        # Break from loop on EOF
        if line == "":
            break

        testMO = test.match(line)

        a = testMO.group(1)

        b = testMO.group(2)

        a = ' ' + a[:len(a)]

        b = ' ' + b[:len(b)]

        c = lcsLength(a, b)

        solution = constructLCS(a, b, c)

        print(solution)


main()









