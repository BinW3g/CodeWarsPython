# codewars challenge link
# https://www.codewars.com/kata/5519a584a73e70fa570005f5
# help with https://www.youtube.com/watch?v=xwM8PGBYazM

import numpy as np


def smallest_multiple_of_n_geq_m(n, m):
    return m + ((n - (m % n)) % n)


class Primes:
    @staticmethod
    def stream():
        dtype = np.int64
        primes = np.array([2, 3, 5, 7], dtype=dtype)
        end_segment = 1
        dtype_max = np.iinfo(dtype).max
        n = 100
        while len(primes) < 1000000:
            k = end_segment
            n = min(n, len(primes) - 1 - k)
            p, q = int(primes[k]), int(primes[k + n])
            segment_min, segment_max = p * p, q * q - 1
            if segment_max > dtype_max:
                raise RuntimeError("overflow, use a larger dtype or pure python implementation")

            segment_len = segment_max - segment_min + 1
            is_prime = np.full(shape=segment_len, fill_value=True, dtype=bool)
            for pk in primes[:k + n]:
                pk = int(pk)
                start = smallest_multiple_of_n_geq_m(pk, segment_min)
                is_prime[start - segment_min::pk] = False

            segment = np.arange(p * p, q * q, dtype=dtype)
            new_primes = segment[is_prime]
            try:
                old_len = len(primes)
                primes.resize(old_len + len(new_primes))
                primes[old_len:] = new_primes
            except ValueError:
                primes = np.concatenate((primes, new_primes))
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
