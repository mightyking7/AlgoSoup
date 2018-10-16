

def mystery(n, a):

    if n == 0:
        return 0

    tmp1 = mystery(n / 2, a)

    tmp2 = 0

    for i in xrange(1, (n/2) + 1):
        tmp2 = tmp2 + a

    if n % 2 == 1:
        return tmp1 + tmp2 + a

    else:
        return tmp1 + tmp2


def main():

    val1 = mystery(2, 3)

    val2 = mystery(1, 2)

    val3 = mystery(20, 10)

    print val1, val2, val3

'''
Entry point
'''

main()

