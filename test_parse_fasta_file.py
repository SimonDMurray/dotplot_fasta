from reading_files import parse_fasta_file
from test_lines_from_file import filename_in_this_directory


def test_read_from_simple_fasta_dot_txt():
    ATCG_fasta_dot_txt = filename_in_this_directory('ATCG_fasta.txt')
    ids, seqs = parse_fasta_file(ATCG_fasta_dot_txt)
    assert ids == ['1']
    assert seqs == ['ATCG']

def test_read_from_rosalind_sample_dot_txt():
    ATCG_fasta_dot_txt = filename_in_this_directory('ATCG_fasta.txt')
    ids, seqs = parse_fasta_file(ATCG_fasta_dot_txt)
    assert ids == ['1']
    assert len(seqs) == 1 

def test_function_has_docstring():
    assert len(parse_fasta_file.__doc__) > 0
