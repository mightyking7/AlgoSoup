'''
Utilizes Dynamic programming to find the least common
sub-sequence between two strands of DNA, whose elements
have an alphabet of A-Z.
'''

'''
Computes longest common sub-sequence
'''


def lcsLength(A, B):
    m = len(A)

    n = len(B)

    # stores optimal sub-problems previously computed
    c = [[]]

    tmpArray = []

    for i in range(0, m):
        tmpArray.append(0)

    c.append(tmpArray)

    for i in range(n, 0):
        tmpArray.append(0)

    c.append(tmpArray)

    for i in range(0, m):

        for j in range(0, n):

            # if the elements match, add one to LCS thus far
            if A[i] == B[i]:

                c[i][j] = c[i - 1][j - 1] + 1

            # find the LCS by computing max( c[i-1][j], c[i][j-1] )
            elif c[i - 1][j] > c[i][j - 1]:

                c[i][j] = c[i - 1][j]

            else:
                c[i][j] = c[i][j - 1]

    return c


def constructLCS():

    
