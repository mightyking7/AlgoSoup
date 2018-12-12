'''
Purpose:
    Utilizes Dynamic programming to find the least common
    sub-sequence between two strings

Parameters:
    A - String to compare
    B - String to compare

Return:
   Table lengths for sequences A and B
'''
def lcsLength(A, B):

    m = len(A)

    n = len(B)

    # overlaying sub-problems
    c = [[0 for j in range(n)] for i in range(m)]

    # determine the LCS
    for i in range(1, m):

        for j in range(1, n):

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

    sol = ""

    while i > 0 and j > 0:

        if A[i] == B[j]:
            sol = A[i] + sol
            i -= 1
            j -= 1

        elif C[i - 1][j] >= C[i][j - 1]:
            i -= 1

        else:
            j -= 1

    return sol