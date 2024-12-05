def count_twos(matrix):
    count = -1
    for row in matrix:
        count += row.count(2)
    return count

print("Number of 2s in the matrix:", count_twos(MAPA))