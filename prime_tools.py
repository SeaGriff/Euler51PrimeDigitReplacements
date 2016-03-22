""" Provides a variety of useful tools related to primes, including implementing the RabinMiller primality test with
the first seven primes, which is provably correct for inputs < 3.4 * 10^14. All inputs are assumed to be in this range.

METHODS PROVIDED:
isPrime: Checks to see if a positive int is prime.
nextPrime: Gives the first prime larger than a given positive int.
getPrimeSet: Gives a set of all the primes in some range.
getPrimeList: Gives a list of all the primes in some range. """

# Imports
import math

# CONSTANTS
PRIME_SET = {2,3,5,7,11,13,17}

""" getPrimeSet and getPrimeList build sets or lists of primes in a given range, using the buildPrimeCollection
function. With one argument, they build their collections up to x1. With two, they return a collection of all primes
from x1 inclusive to x2 exclusive. """
def getPrimeSet(x1, x2=0):
    return buildPrimeCollection(x1, x2, False)

def getPrimeList(x1, x2=0):
    return buildPrimeCollection(x1, x2, True)

# If the listFlag parameter is true, builds a list. Otherwise, builds a set.
def buildPrimeCollection(x1, x2, listFlag):
    if listFlag == False:
        result = set()
    else:
        result = []
    if x2 == 0:
        latest = 1
        maximum = x1
    else:
        latest = x1 - 1
        maximum = x2
    while latest < maximum:
        latest = nextPrime(latest)
        if latest < maximum:
            if listFlag == False:
                result.add(latest)
            else:
                result.append(latest)
    return result

# Counts the factors of two that divide the passed in input
def countFactorsOfTwo(x):
    result = 0
    while math.fmod(x,2) == 0:
        x /= 2.0
        result += 1
    return result

""" Checks to see if the input is prime.
Accepts: int x
Restrictions: 3.4 * 10^14 > x """

def isPrime(x):
    if x in PRIME_SET:
        return True
    if x < 2:
        return False
    for p in PRIME_SET:
        if x % p == 0:
            return False
    evenPower = int(countFactorsOfTwo(x - 1))
    oddFactor = int((x - 1) / 2**evenPower)
    for p in [prime for prime in PRIME_SET if prime < x]:
        probablyPrime = False
        if pow(p,oddFactor,x) == 1:
            probablyPrime = True
        else:
            for j in range(0,evenPower):
                if pow(p,(2**j)*oddFactor,x) == x-1:
                    probablyPrime = True
                    break
        if probablyPrime == False:
            return False
    return True

""" Finds the next largest prime.
Accepts: int n
Restrictions: 3.4 * 10^14 > n > 0. May return a false positive for inputs greater than the least prime less
than 3.4 * 10^14
Returns: the least int p such that p > n """

def nextPrime(n):
    n += 1
    while not isPrime(n):
        n += 1
    return n