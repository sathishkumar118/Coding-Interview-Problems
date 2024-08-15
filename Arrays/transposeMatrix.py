def transposeMatrix(matrix):
    res = []
    for i in range(len(matrix[0])):
        curr = []
        for j in range(len(matrix)):
            curr.append(matrix[j][i])
        res.append(curr)
    return res
