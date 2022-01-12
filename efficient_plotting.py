import argparse
from colorama import Fore, Style


PARSER = argparse.ArgumentParser()
PARSER.add_argument("-basic", help="produces basic dotplot without changess", action="store_true")
PARSER.add_argument("-colour", help="produces dotplot where letters not on diagnonals are blacked out", action="store_true")
PARSER.add_argument("-compliment", help="produces mapped compliment base pairing dotplot", action="store_true")
PARSER.add_argument('-file1', help="first sequence that will be used as x axis in the dotplot", dest='seq1', action='store')
PARSER.add_argument('-file2', help="second sequence that will be used as the y axis in the dotplot", dest='seq2', action='store')
PARSER.add_argument("-filter", help="produces dotplot where diagonals are capitalised and other letters arent", action="store_true")
PARSER.add_argument("-palindrome", help="produces dotplot where letters are repalced with ascii characters and palindromes are checked in both diagonal directions", action="store_true")
ARGS = PARSER.parse_args()


def prepare_filtering(matrix, seq1, seq2):
    '''
    Determines which type of filtering should occur
    depending on arguments passed on command line.
    Iterates through matrix to access each value
    in the matrix
    '''
    print_matrix = [[" " for x in range(len(seq1))] for y in range(len(seq2))]
    column_limit = len(seq1) - 1
    row_limit = len(seq2) - 1
    for row in range(len(seq2)):
        for column in range(len(seq1)):
            if ARGS.compliment:
                seq1_col = seq1[column]
                seq2_row = seq2[row]
                print_matrix = compliment_filtering(seq1_col, seq2_row, row, column, print_matrix)
            else:
                value = matrix[row][column]
                if value != " ":
                    if ARGS.palindrome:
                        print_matrix = palindrome_filtering(value, row, row_limit, column, column_limit, matrix, print_matrix)
                    else:
                        print_matrix = filtering(value, row, row_limit, column, column_limit, matrix, print_matrix)
    return print_matrix


def filtering(value, row, row_lim, column, column_lim, matrix, print_matrix):
    '''
    compares the next diagonal positions in the matrix,
    forwards 1 and backwards 1 to calculate diagnoals
    '''
    if row == 0 and column != column_lim:
        next = matrix[row + 1][column + 1]
        print_matrix = single_choice(next, value, row, column, print_matrix)
    elif row == row_lim and column != 0:
        prev = matrix[row - 1][column - 1]
        print_matrix = single_choice(prev, value, row, column, print_matrix)
    elif row == 0 and column == column_lim or row == row_lim and column == 0:
        print_matrix = edit_matrix_no_match(value, row, column, print_matrix)
    elif column == 0 and row != 0 or column == 0 and row != row_lim:
        next = matrix[row + 1][column + 1]
        print_matrix = single_choice(next, value, row, column, print_matrix)
    elif column == column_lim and row != 0 or column == column_lim and row != row_lim:
        prev = matrix[row - 1][column - 1]
        print_matrix = single_choice(prev, value, row, column, print_matrix)
    elif column != 0 or column != column_lim and row != 0 and row != row_lim:
        next = matrix[row + 1][column + 1]
        previous = matrix[row - 1][column - 1]
        print_matrix = double_choice(next, previous, value, row, column, print_matrix)
    return print_matrix


def palindrome_filtering(value, row, row_limit, column, column_limit, matrix, print_matrix):
    '''
    compares forwards and backwards one
    along both diagonals in order to
    calculate palindromes
    '''
    if row == 0 and column == 0:
        next_f = matrix[row + 1][column + 1]
        print_matrix = single_choice(next_f, value, row, column, print_matrix)
    elif row == 0 and column == column_limit:
        n_p = matrix[row + 1][column - 1]
        print_matrix = single_choice_pal(n_p, value, row, column, print_matrix)
    elif row == row_limit and column == column_limit:
        prev_f = matrix[row - 1][column - 1]
        print_matrix = single_choice(prev_f, value, row, column, print_matrix)
    elif row == row_limit and column == 0:
        previous_p = matrix[row - 1][column + 1]
        print_matrix = single_choice_pal(previous_p, value, row, column, print_matrix)
    elif row != 0 and column == 0 or row != row_limit and column == 0:
        next_f = matrix[row + 1][column + 1]
        previous_p = matrix[row - 1][column + 1]
        print_matrix = double_choice_pal(next_f, previous_p, value, row, column, print_matrix)
    elif row == 0 and column != 0 or row == 0 and column != column_limit:
        next_f = matrix[row + 1][column + 1]
        next_p = matrix[row + 1][column - 1]
        print_matrix = double_choice_pal(next_f, next_p, value, row, column, print_matrix)
    elif row != 0 and column == column_limit or row != row_limit and column == column_limit:
        previous_f = matrix[row - 1][column - 1]
        next_p = matrix[row + 1][column - 1]
        print_matrix = double_choice_pal(previous_f, next_p, value, row, column, print_matrix)
    elif row == row_limit and column != 0 or row == row_limit and column != column_limit:
        prev_f = matrix[row - 1][column - 1]
        prev_p = matrix[row - 1][column + 1]
        print_matrix = double_choice_pal(prev_f, prev_p, value, row, column, print_matrix)
    elif row != 0 and row != row_limit and column != 0 and column != column_limit:
        next_f = matrix[row + 1][column + 1]
        next_p = matrix[row + 1][column - 1]
        prev_f = matrix[row - 1][column - 1]
        prev_p = matrix[row - 1][column + 1]
        print_matrix = quad_choice(next_f, next_p, prev_f, prev_p, value, row, column, print_matrix)
    return print_matrix


def compliment_filtering(seq1_c, seq2_r, row, col, print_matrix):
    '''
    matches complimentary base pairs
    in sequence provided and indicates
    these matches
    '''
    if seq2_r == 'A' and seq1_c == 'T' or seq2_r == 'A' and seq1_c == 'U':
        print_matrix[row][col] = chr(92)
    elif seq2_r == 'T' and seq1_c == 'A' or seq2_r == 'U' and seq1_c == 'A':
        print_matrix[row][col] = chr(92)
    elif seq2_r == 'C' and seq1_c == 'G':
        print_matrix[row][col] = chr(92)
    elif seq2_r == 'G' and seq1_c == 'C':
        print_matrix[row][col] = chr(92)
    return print_matrix


def edit_matrix_match(val, row, col, print_matrix):
    '''
    filters what to edit in the matrix
    if there is a match depending
    on arguments passed. Default is ascii
    '''
    if ARGS.filter or ARGS.colour:
        print_matrix[row][col] = val
    elif ARGS.basic:
        print_matrix[row][col] = val
    else:
        print_matrix[row][col] = chr(92)
    return print_matrix


def edit_matrix_no_match(val, row, col, print_matrix):
    '''
    Filters what to edit in the matrix
    if there is no match, depending
    on arguments passed. Default is ascii
    '''
    if ARGS.filter or ARGS.colour:
        val = val.lower()
        if ARGS.colour:
            print_matrix[row][col] = Fore.BLACK + val + Style.RESET_ALL
        elif ARGS.filter:
            print_matrix[row][col] = val
    elif ARGS.basic:
        print_matrix[row][col] = val
    else:
        print_matrix[row][col] = chr(46)
    return print_matrix


def edit_matrix_match_pal(row, col, print_matrix):
    '''
    edits matrix if palindrome found
    on opposite diagonal
    '''
    print_matrix[row][col] = chr(47)
    return print_matrix


def single_choice(direction, val, row, col, print_matrix):
    '''
    calculates if there is a match
    diagnoally in one direction
    '''
    if direction != ' ':
        print_matrix = edit_matrix_match(val, row, col, print_matrix)
    else:
        print_matrix = edit_matrix_no_match(val, row, col, print_matrix)
    return print_matrix


def single_choice_pal(direction, val, row, col, print_matrix):
    '''
    calculates if there is match
    on reverse diagonal in one
    direction
    '''
    if direction != ' ':
        print_matrix = edit_matrix_match_pal(row, col, print_matrix)
    else:
        print_matrix = edit_matrix_no_match(val, row, col, print_matrix)
    return print_matrix


def double_choice(direction, direction_opposite, val, row, col, print_matrix):
    '''
    calculates if there is a match
    in 2 directions diagonally
    '''
    if direction != ' ' or direction_opposite != ' ':
        print_matrix = edit_matrix_match(val, row, col, print_matrix)
    elif direction == ' ' and direction_opposite == ' ':
        print_matrix = edit_matrix_no_match(val, row, col, print_matrix)
    return print_matrix


def double_choice_pal(direction, direction2, val, row, col, print_matrix):
    '''
    calculates if there is a match
    in 2 directions for palindrome
    indetification
    '''
    if direction != " " and direction2 == " ":
        print_matrix = edit_matrix_match(val, row, col, print_matrix)
    elif direction == " " and direction2 != " ":
        print_matrix = edit_matrix_match_pal(row, col, print_matrix)
    else:
        print_matrix = edit_matrix_no_match(val, row, col, print_matrix)
    return print_matrix


def quad_choice(next_f, next_p, prev_f, prev_p, val, row, col, print_matrix):
    '''
    calculates if there is a match
    in 4 directions
    '''
    if next_f == " " and next_p == " " and prev_f == " " and prev_p == " ":
        print_matrix = edit_matrix_no_match(val, row, col, print_matrix)
    elif next_f != " " or prev_f != " " and next_p == " " and prev_p == " ":
        print_matrix = edit_matrix_match(val, row, col, print_matrix)
    elif next_f == " " and prev_f == " " and next_p != " " or prev_p != " ":
        print_matrix = edit_matrix_match_pal(row, col, print_matrix)
    return print_matrix
