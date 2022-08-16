import pytest

from kissues.distinct_letters_count import count_letters_to_delete
from kissues.distinct_letters_count import MAX_N


@pytest.mark.parametrize(
    "s,n",
    [
        ("aaaabbbb", 1),
        ("ccaaffddecee", 6),
        ("eeee", 0),
        ("", 0),
        ("a", 0),
    ],
)
def test_count_letters_to_delete_it_works(s, n):
    assert n == count_letters_to_delete(s)


def test_count_letters_to_delete_bad_s():
    with pytest.raises(ValueError):
        count_letters_to_delete("a" * (MAX_N + 1))
