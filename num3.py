def find_first_zero_row_and_reduce_column(matrix):
    for i, row in enumerate(matrix):
        if all(element == 0 for element in row):
            zero_row_index = i

            for j in range(len(matrix)):
                matrix[j][zero_row_index] /= 2
            return zero_row_index
    return None
rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        element = float(input(f"Введите элемент матрицы [{i}][{j}]: "))
        row.append(element)
    matrix.append(row)

zero_row_index = find_first_zero_row_and_reduce_column(matrix)

if zero_row_index is not None:
    print(f"Первая строка с нулевыми элементами: {zero_row_index}")
    print("Матрица после уменьшения элементов столбца:")
    for row in matrix:
        print(row)
else:
    print("В матрице нет строк, где все элементы равны нулю.")
