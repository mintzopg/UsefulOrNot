def sieve(m, k, weights, values, n):
    # use a bottom up approach (dynamic programming)
    for i in range(0, n + 1):
        for c in range(0, k + 1):
            if c == 0 or i == 0:
                m[c][i] = 0
            elif c < weights[i - 1]:
                m[c][i] = m[c][i - 1]
            else:
                v = values[i - 1]   # temp value
                k_residual = c - weights[i - 1]     # residual capacity
                u = m[k_residual][i - 1]            # residual value
                m[c][i] = max(v + u, m[c][i - 1])
    return m, m[k][n]   # return the dynamic programming matrix and the optimal value


def trace_back(m, k, weights, n):
    # return a list representing xi. e.g. [1, 0, 0, 1] means x1=1, x2=x3=0, x4=1
    sl = []
    while n > 0:
        if m[k][n] != m[k][n - 1]:
            sl.append(1)
            k = k - weights[n - 1]
            n -= 1
        else:
            sl.append(0)
            n -= 1
    sl.reverse()
    return sl

if __name__ == '__main__':
    # k = 7
    # values = [16, 19, 23, 28]
    # weights = [2, 3, 4, 5]

    k = 11
    values = [8, 10, 15, 4]
    weights = [4, 5, 8, 3]

    # Initialize the sieve matrix with zero elements
    n = len(values)
    m = [[0 for i in range(n + 1)] for c in range(k + 1)]

    # call the sieve to get the optimal value
    m, o = sieve(m, k, weights, values, n)
    # print matrix m
    for l in m:
        print(l, sep="\n")
    print("Optimal values = ", o)

    # call the trace_back method to get the items selected in the knapsack
    selected = trace_back(m, k, weights, n)
    print("Items, selected in knapsack: ", selected)
