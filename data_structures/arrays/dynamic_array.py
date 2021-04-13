def dynamicArray(n, queries):
    matrix = [[] for _ in range(n)]
    last_answer = 0
    result = []

    for query_type, x, y in queries:
        index = (x ^ last_answer) % n
        if query_type == 1:
            matrix[index].append(y)
        elif query_type == 2:
            value = matrix[index][y % len(matrix[index])]
            last_answer = value
            result.append(value)

    return result


if __name__ == "__main__":
    n = 2
    queries = [[1, 0, 5], [1, 1, 7], [1, 0, 3], [2, 1, 0], [2, 1, 1]]

    print(dynamicArray(n, queries))