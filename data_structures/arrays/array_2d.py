def hourglassSum(matr):
    HS_SIZE = 3
    max_sum = None

    max_row = len(matr) - HS_SIZE + 1
    for row in range(max_row):
        max_col = len(matr[row]) - HS_SIZE + 1
        for col in range(max_col):
            hs_sum = (
                matr[row][col]
                + matr[row][col + 1]
                + matr[row][col + 2]
                + matr[row + 1][col + 1]
                + matr[row + 2][col]
                + matr[row + 2][col + 1]
                + matr[row + 2][col + 2]
            )
            if max_sum is None or hs_sum > max_sum:
                max_sum = hs_sum

    return max_sum


if __name__ == "__main__":
    input_data = [
        [-9, -9, -9, 1, 1, 1],
        [0, -9, 0, 4, 3, 2],
        [-9, -9, -9, 1, 2, 3],
        [0, 0, 8, 6, 6, 0],
        [0, 0, 0, -2, 0, 0],
        [0, 0, 1, 2, 4, 0],
    ]
    print(hourglassSum(input_data))