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

            # find the LCS by computing max(c[i-1][j], c[i][j-1])
            elif c[i - 1][j] > c[i][j - 1]:
                c[i][j] = c[i - 1][j]

            else:
                c[i][j] = c[i][j - 1]

    return c


'''
Purpose:
    Used to construct the least common sub-sequence
    from a memoized table of subsequence lengths

Parameters:
    A - String
    B - String
    C - table of longest sub-sequence lengths
    
Return:
    The Longest common sub-sequence between A and B
'''
def constructLCS(A, B, C):

    i = len(A) - 1

    j = len(B) - 1

    sol = ""    # solution

    while i > 0 and j > 0:

        if A[i] == B[j]:
            #TODO, optimize concatenation
            sol = A[i] + sol
            i -= 1
            j -= 1

        elif C[i - 1][j] >= C[i][j - 1]:
            i -= 1

        else:
            j -= 1

    return sol





'''
Test LCS
'''
a = [None, 'a', 'g', 'c', 'a', 't']

b = [None, 'g', 'a', 'c']

c = lcsLength(a, b)

lcs = constructLCS(a, b, c)

print(lcs)