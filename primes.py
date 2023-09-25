"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes<=0:
        raise ValueError
    list = []
    next_prime = 2
    for i in range(0,number_of_primes):
        list.append(next_prime)
        next_prime = next_prime + 1
        while not isPrime(next_prime):
            next_prime = next_prime+1
    return list

def isPrime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True
