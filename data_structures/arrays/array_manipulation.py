# Naive solution, fails due to Runtime Error
# def arrayManipulation(n, queries):
#     array = [0] * n
#     for query in queries:
#         a = query[0] - 1
#         b = query[1]
#         k = query[2]
#         for i in range(a, b):
#             array[i] += k
#         print(array)
#     return max(array)


# Optimized solution, fails due to long execution time
# def arrayManipulation(n, queries):
#     queries = sorted(queries, key=lambda q: (q[0], q[1]))
#     max_value = 0
#     for i in range(n):
#         curr_sum = 0
#         j = 0
#         while j < len(queries):
#             query = queries[j]
#             a = query[0] - 1
#             b = query[1] - 1
#             k = query[2]

#             # Current range
#             if a <= i and b >= i:
#                 curr_sum += k
#             # Past range, useless
#             elif a < i and b < i:
#                 queries.pop(j)
#                 j -= 1
#             else:
#                 break
#             j += 1
#         if curr_sum > max_value:
#             max_value = curr_sum

#     return max_value

# Best solution, approach taken from HackerRank's "discussions"
def arrayManipulation(n, queries):
    array = [0] * (n + 1)
    for query in queries:
        a = query[0] - 1
        b = query[1]
        k = query[2]
        array[a] += k
        array[b] -= k

    max_value = 0
    curr_value = 0
    for item in array:
        curr_value += item
        if curr_value > max_value:
            max_value = curr_value

    return max_value


if __name__ == "__main__":
    queries = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
    print(arrayManipulation(5, queries))
