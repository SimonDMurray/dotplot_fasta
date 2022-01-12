import os
from reading_files import lines_from_file


def test_read_lines_from_simple_fasta_dot_txt():
    ATCG_fasta_dot_txt = filename_in_this_directory('ATCG_fasta.txt')
    assert lines_from_file(ATCG_fasta_dot_txt) == ['>1', 'ATCG']


def test_read_lines_from_rosalind_sample_dot_txt():
    ATCG_fasta_dot_txt = filename_in_this_directory('ATCG_fasta.txt')
    assert len(lines_from_file(ATCG_fasta_dot_txt)) == 2


def test_function_has_docstring():
    assert len(lines_from_file.__doc__) > 0


def filename_in_this_directory(filename):
    """
    returns the absolute path for file filename
    in the same directory as this file.

    Needed because tests need to run independently from
    any directory

    Raises:
        RuntimeError if the filename does not exist
    """
    this_directory = os.path.dirname(os.path.abspath(__file__))
    test_filename = os.path.join(this_directory, filename)
    if not os.path.isfile(test_filename):
        raise RuntimeError('test setup failed to find file:' + test_filename)
    return test_filename
