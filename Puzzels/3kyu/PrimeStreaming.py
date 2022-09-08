# codewars challenge link
# https://www.codewars.com/kata/5519a584a73e70fa570005f5

from itertools import repeat

def smallest_multiple_of_n_geq_m(n, m):
    return m + ((n - (m % n)) % n)


class Primes:
    @staticmethod
    def stream():
        primes = [2, 3, 5, 7]
        end_segment = 1
        n = 100
        while len(primes) < 1000000:
            k = end_segment
            n = min(n, len(primes) - 1 - k)
            p = primes[k]
            q = primes[k + n]
            segment = range(p * p, q * q)
            segment_min = min(segment)
            segment_len = len(segment)
            is_prime = [True] * segment_len

            for i in range(k + n):
                pk = primes[i]
                start = smallest_multiple_of_n_geq_m(pk, segment_min)
                is_prime[start - segment_min::pk] = repeat(False, len(range(start - segment_min, segment_len, pk)))

            primes.extend([x for x, it_is_prime in zip(segment, is_prime) if it_is_prime])
            end_segment += n
        return iter(primes)


def verify(from_n, *vals):
    stream = Primes.stream()
    for _ in range(from_n):
        next(stream)
    for v in vals:
        print(next(stream) == v)


if __name__ == '__main__':
    verify(0, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
    verify(10, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71)
    verify(100, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601)
    verify(1000, 7927, 7933, 7937, 7949, 7951, 7963, 7993, 8009, 8011, 8017)
