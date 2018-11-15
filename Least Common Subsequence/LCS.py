'''
Utilizes Dynamic programming to find the least common
sub-sequence between two variable length input strings
'''

#TODO use lists comprehension
def lcsLength(A, B):

    m = len(A) - 1

    n = len(B) - 1

    # stores previously computed sub-problems
    c = [[]]

    # c is a new table
    for i in range(0, m + 1):

        tmpArray = []

        for j in range(0, n + 1):
            tmpArray.append(0)

        c.insert(i, tmpArray)

    # determine the LCS

    for i in range(1, m + 1):

        for j in range(1, n + 1):

            # if the elements match, add one to LCS thus far
            if A[i] == B[j]:
                c[i][j] = c[i - 1][j - 1] + 1

            # find the LCS by computing max( c[i-1][j], c[i][j-1] )
            elif c[i - 1][j] > c[i][j - 1]:
                c[i][j] = c[i - 1][j]

            else:
                c[i][j] = c[i][j - 1]

    return c


'''
Test LCS
'''

a = [None, 'a', 'g', 'c', 'a', 't']

b = [None, 'g', 'a', 'c']

c =

c = lcsLength(a, b)