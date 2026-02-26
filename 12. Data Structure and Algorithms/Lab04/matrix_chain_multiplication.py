"""
cost[i, j] = 0    if i == j
cost[i, j] = min(cost[i, k] + cost[k+1, j] + dim[i-1] * dim[k] * dim[j]) if i < j
"""

def matrix_chain(p):
    n = len(p) - 1
    costs = [[0] * n for _ in range(n)]
    splits = [[0] * n for _ in range(n)]

    for l in range(2, n + 1): 
        for i in range(n - l + 1):
            j = i + l - 1
            costs[i][j] = float('inf')
            for k in range(i, j):
                q = costs[i][k] + costs[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if q < costs[i][j]:
                    costs[i][j] = q
                    splits[i][j] = k

    return costs, splits

def print_chain(splits, i, j):
    # print(splits)
    if i == j:
        print(f"A{i+1}", end = "")
        return 
    
    print("(", end="")
    print_chain(splits, i, splits[i][j])
    print(" X ", end = '')
    print_chain(splits, splits[i][j] + 1, j)
    print(")", end = '')

if __name__ == "__main__":
    dimensions = [5, 4, 6, 2, 7]  # (5 * 4) * (4 * 6) * (6 * 2) * (2 * 7)
    costs, splits = matrix_chain(dimensions)
    print("Minimum number of multiplications is:", costs[0][len(dimensions) - 2])
    print_chain(splits, 0, len(dimensions) - 2)