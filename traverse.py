def amorcito(arr: list):
    start_row = 0
    end_row = len(arr) - 1
    start_col = 0
    end_col = len(arr[0]) - 1
    output = []

    while start_row <= end_row and start_col <= end_col:
        for col in range(start_col, end_col + 1):
            output.append(arr[start_row][col])

        for row in range(start_row + 1, end_row + 1):
            output.append(arr[row][end_col])

        for col in reversed(range(start_col, end_col)):
            if start_row == end_row:
                break
            output.append(arr[end_row][col])

        for row in reversed(range(start_row + 1, end_row)):
            if start_col == end_col:
                break
            output.append(arr[row][start_col])

        start_row += 1
        end_row -= 1
        start_col += 1
        end_col -= 1

    return output


matrix = [
    [1, 2, 3, 4],
    [8, 9, 4, 5],
    [7, 6, 5, 8]
]

amorcito(matrix)
