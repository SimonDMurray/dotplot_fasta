def plotting(print_matrix, seq1, seq2):
    '''
    plots matrix provided in a dotplot format
    '''
    counter = 0
    number = len(seq1)
    print("  ", end="")
    for letter in seq1:
        print(letter, end="")
    print("")
    print(" " + "+" + number * "-")
    for row in print_matrix:
        row = "".join(row)
        print(seq2[counter] + "|" + row)
        counter = counter + 1
    return print_matrix, counter
