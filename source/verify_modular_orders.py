"""Reproduce the elementary checks described in the accompanying manuscript.

All calculations use integers; no plotting packages or external data required.
"""
from collections import Counter
from math import gcd


def order_by_repetition(a: int, n: int) -> int:
    """Find the first return to zero by repeatedly adding a modulo n."""
    r = 0
    for k in range(1, n + 1):
        r = (r + a) % n
        if r == 0:
            return k
    raise AssertionError("Unexpected failure to return to identity")


def totient(m: int) -> int:
    return sum(gcd(a, m) == 1 for a in range(m))


def cycle_lengths(a: int, n: int) -> list[int]:
    visited = set()
    lengths = []
    for start in range(n):
        if start in visited:
            continue
        current = start
        length = 0
        while current not in visited:
            visited.add(current)
            length += 1
            current = (current + a) % n
        assert current == start, (a, n, start, current)
        lengths.append(length)
    return lengths


def main() -> None:
    tested = 0
    for n in range(2, 501):
        counts = Counter()
        for a in range(n):
            expected = n // gcd(a, n)
            observed = order_by_repetition(a, n)
            assert expected == observed, (a, n, expected, observed)
            counts[expected] += 1
            # The translation map has gcd(a,n) cycles of the same length.
            lengths = cycle_lengths(a, n)
            assert len(lengths) == gcd(a, n), (a, n, lengths)
            assert set(lengths) == {expected}, (a, n, lengths)
            tested += 1
        for m in range(1, n + 1):
            if n % m == 0:
                assert counts[m] == totient(m), (n, m, counts[m], totient(m))
        assert sum(counts.values()) == n
    print(f"PASS: {tested:,} residue/modulus pairs checked, 2 <= n <= 500")
    print("PASS: direct iteration, gcd formula, cycle counts and totient distribution")
    for n in (10, 12, 100):
        print(f"Z_{n}: " + ", ".join(f"ord({a})={n//gcd(a,n)}" for a in range(min(n, 10))))


if __name__ == "__main__":
    main()
