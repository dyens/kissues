MAX_N = 200_000


def gen_odd_word(n: int) -> str:
    """Gen odd word.

    We only care about oddnes letters occurance, so lets return
    "aaa..." if n is odd, "aaa..b is n is even.

    :param n: string length
    :return: generated string
    """
    if not 1 <= n <= MAX_N:
        raise ValueError("Not valid n")
    if n % 2:
        return "a" * n + "b"
    return "a" * n
