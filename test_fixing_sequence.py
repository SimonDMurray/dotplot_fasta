from reading_files import fixing_sequence

def test_function_has_docstring():
    assert len(fixing_sequence.__doc__) > 0

def test_removes_list_characters():
    sequence = fixing_sequence("['ATCGGCTA']")
    assert sequence == 'ATCGGCTA'
def test_uppercase():
    string = 'abcde'
    sequence = fixing_sequence(string)
    assert sequence == string.upper()
