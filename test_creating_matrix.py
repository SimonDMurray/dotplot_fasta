from generating_matrix import creating_matrix

def test_function_has_docstring():
    assert len(creating_matrix.__doc__) > 0

def test_function_creates_matrix():
    matrix = creating_matrix('ATCG', 'CGTA')
    assert len(matrix) == 4

def test_function_orders_matrix_correctly():
    matrix = creating_matrix('ATCG', 'CTGA')
    assert matrix[1][1] == 'T'
