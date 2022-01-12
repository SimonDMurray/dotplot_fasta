from plotting_dotplot import plotting

def test_function_has_docstring():
    assert len(plotting.__doc__) > 0

def test_handles_matrix():
    matrix = [['A' for i in range(3)] for i in range(2)]
    print_matrix, counter = plotting(matrix, 'AAA', 'AA')
    assert print_matrix[1][2] == 'A' and print_matrix[0].count('A') == 3
    
def test_plots_correct():
    matrix = [['A' for i in range(3)] for i in range(1)]
    print_matrix, counter = plotting(matrix, 'AAA', 'A')
    assert counter == len('A')
