def creating_matrix(seq1, seq2):
    '''
    generates matrix from the
    strings formed from the
    2 input files
    '''
    matrix = [[" " for x in range(len(seq1))] for y in range(len(seq2))]
    for index1, value1 in enumerate(seq2):
        for index2, value2 in enumerate(seq1):
            if value1 == value2:
                matrix[index1][index2] = value1
            else:
                matrix[index1][index2] = " "
    return matrix
