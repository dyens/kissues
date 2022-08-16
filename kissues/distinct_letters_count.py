from collections import Counter

MAX_N = 300_000


def count_letters_to_delete(s: str) -> int:
    """Count letters to delete.

    Count the minimum number of letters that must be
    deleted from a word to create a word in which no
    two letters occur the same number of times.

    :param s: input string
    :return: number letters to remove
    """
    if len(s) > MAX_N:
        raise ValueError("So long string")

    letters = Counter(s)
    freqs = sorted(letters.values())

    to_delete = 0

    # we need remove letters only if we have > 2 freq in freqs
    while len(freqs) > 1:
        max_freq = freqs.pop()
        prev_freq = freqs[-1]
        if max_freq == prev_freq:
            if max_freq > 1:
                freqs.append(max_freq - 1)
                freqs.sort()
            to_delete += 1
    return to_delete
