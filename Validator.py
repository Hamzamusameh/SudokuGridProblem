input = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

def validator(input):
    allowedInputs = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    validSum = 45
    subGrids = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(9):
        rowSum = 0
        columnSum = 0
        for j in range(9):
            if input[i][j] in allowedInputs and input[j][i] in allowedInputs:
                rowSum += input[i][j]
                columnSum += input[j][i]
                if j % 3 == 2:
                    subGrids[i // 3][j // 3] += sum(input[i][j - 2: j + 1])
                if i % 3 == 2 and j % 3 == 2:
                    if subGrids[i // 3][j // 3] != validSum:
                        return f'False @i={i},j={j} invalid square sum {subGrids[i // 3][j // 3]}'
                        print('current grid', subGrids)
            else:
                return f'False @i={i},j={j} not allowed input'
        if rowSum != validSum or columnSum != validSum:
            return f'False @i={i} row_sum = {rowSum} - column_sum = {columnSum}'
    return True

print(validator(input))
