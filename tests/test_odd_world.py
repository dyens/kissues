import pytest
from kissues.odd_world import MAX_N, gen_odd_word
from collections import Counter


def test_gen_odd_word_it_works():
    word = gen_odd_word(3)
    letters = Counter(word)
    for letter in letters:
        assert letters[letter] % 2 == 1


@pytest.mark.parametrize("n", [0, -10, MAX_N + 1])
def test_gen_odd_world_bad_n(n):
    with pytest.raises(ValueError):
        gen_odd_word(n)
