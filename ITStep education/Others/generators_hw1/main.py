import re


def isprime_v1(n):
    prime_list = [i for i in range(n) if re.compile(r'^1?$|^(11+)\1+$').match('1' * i) is None]
    return print(prime_list)


def isprime_v2(n):
    prime_list = [i for i in range(2, n) if not [j for j in range(2, i) if not i % j]]
    return print(prime_list)


isprime_v1(100)
isprime_v2(100)