"""Test module for coverviz.preprocessing."""
from pathlib import Path

import coverviz.preprocessing as cvp

FIXTURES_DIR = Path(__file__).parent / "fixtures"


def test_load_json():
    """Test loading json."""
    actual = cvp.load_json(FIXTURES_DIR / "load_json.json")
    expected = {"test": "test_value"}
    assert actual == expected


def test_clean_up_json():
    """Test cleaning up json."""
    input_js = {'files': {'lib/module/file.py': {'summary': {'covered_lines': 12,
                                                             'num_statements': 14,
                                                             'excluded_lines': 0}},
                          'lib/module/__init__.py': {'summary': {'covered_lines': 10,
                                                                 'num_statements': 10,
                                                                 'excluded_lines': 0}},
                          'lib/tests/test_file.py': {'summary': {'covered_lines': 6,
                                                                 'num_statements': 12,
                                                                 'excluded_lines': 0}}}}
    actual = cvp.clean_up_json(input_js)
    expected = {'lib': {'module': {'file.py': [12, 14], '__init__.py': [10, 10]},
                        'tests': {'test_file.py': [6, 12]}}}
    assert actual == expected


def test_identify_modules():
    """Test module identification and summary of coverage."""
    input_dic = {'lib': {'module': {'file.py': [12, 14], '__init__.py': [10, 10]},
                         'tests': {'test_file.py': [6, 12]}}}
    actual = cvp.identify_modules(input_dic, "")
    expected = [['/lib', [22, 24]], ['/lib/module', [22, 24]],
                ['/lib/module/file.py', [12, 14]], ['/lib/module/__init__.py', [10, 10]]]
    assert actual == expected


def test_identify_modules2():
    """Test module identification of the names."""
    pass


def test_generate_coverage():
    """Test generating the module coverage (num lines coverred and total)."""
    pass


def test_split_coverage():
    """Test generation of trie structure for coverage."""
    pass


def test_generate_coverage_level():
    """Test coverage by module and file generation."""
    pass
