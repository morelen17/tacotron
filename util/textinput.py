import re
import unicodedata
from util import cmudict, numbers

# Input russian alphabet (77 symbols)
_pad           = '_'
_eos           = '~'
_uppercase     = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
_lowercase     = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
_punctuation   = '!\'(),-.:;?'
_space         = ' '

_valid_input_chars = _uppercase + _lowercase + _punctuation + _space  # 77
# _trans_table = str.maketrans({chr(i): ' ' for i in range(256) if chr(i) not in _valid_input_chars})

_normal_symbols = _pad + _eos + _valid_input_chars  # 79
_num_normal_symbols = len(_normal_symbols)
_char_to_id = {c: i for i, c in enumerate(_normal_symbols)}
_id_to_char = {i: c for i, c in enumerate(_normal_symbols)}
_num_symbols = _num_normal_symbols
_whitespace_re = re.compile(r'\s+')


def num_symbols():
    """Returns number of symbols in the alphabet."""
    return _num_symbols


def to_sequence(text, force_lowercase=True, expand_abbreviations=True):
    """Converts a string of text to a sequence of IDs for the symbols in the text"""
    text = text.strip()
    text = text.replace('"', '')
    sequence = []
    sequence += _text_to_sequence(text, force_lowercase, expand_abbreviations)
    sequence.append(_char_to_id[_eos])
    return sequence


def to_string(sequence, remove_eos=False):
    """Returns the string for a sequence of characters."""
    s = ''
    for sym in sequence:
        s += _id_to_char[sym]
    s = s.replace('}{', ' ')
    if remove_eos and s[-1] == _eos:
        s = s[:-1]
    return s


def _text_to_sequence(text, force_lowercase, expand_abbreviations):
    text = _remove_extra_symbols(text)
    if force_lowercase:
        text = text.lower()
    text = re.sub(_whitespace_re, ' ', text)
    return [_char_to_id[c] for c in text]


def _remove_extra_symbols(text):
    processed = ''
    for char in text:
        processed += char if char in _valid_input_chars else ''
    return processed
