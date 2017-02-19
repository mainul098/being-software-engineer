# complexity O(2**n)


def lcs(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    elif X[m - 1] == Y[n - 1]:
        return 1 + lcs(X, Y, m - 1, n - 1)
    else:
        return max(lcs(X, Y, m - 1, n), lcs(X, Y, m, n - 1))


def main():
    X = "AGGTAB"
    Y = "GXTXAYB"
    print("Length of LIS is", lcs(X, Y, len(X), len(Y)))


if __name__ == '__main__':
    main()