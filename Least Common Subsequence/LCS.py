'''
Utilizes Dynamic programming to find the least common
sub-sequence between two variable length input strings
'''
def lcsLength(A, B):

    m = len(A) - 1

    n = len(B) - 1

    # table for previously computed sub-problems
    c = [[0 for j in range(n + 1)] for i in range(m + 1)]

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

c = lcsLength(a, b)