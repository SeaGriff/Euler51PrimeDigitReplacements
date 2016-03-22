""" Solves project euler problem 51 (the first one rated as reasonably difficult).
We iterate across lengths of primes first - that is, we check all the k length primes, then all the k+1 length
primes, etc.
We mark digits of a k length prime to be replaced by referencing a k length list of 1s and 0s, with 1 at an index i
indicating the i-th digit of the prime should be replaced. Thus for example if consider the prime 131 and the list [
0,1,1], we intend to replace the first and second digits from the right of 131.
Note that since we wish to determine 8 primes, if the last digit is marked for replacement at least one of our
replacements will be even and we do not have a solution. We omit such cases. It is then easy to see that two digit
numbers need not be checked.
"""

# Imports
from prime_tools import getPrimeSet, isPrime
from sys import exit
import itertools

# Constants
NUM_PRIMES_DESIRED = 8
MIN_DIGITS = 7

""" Takes an int, a permutation list (ie one indicating which digits of the int are to be replaced), and a parameter
indicating
what to
replace those digits with. Performs the replacement and returns the result.
Accepts: int num, list<int> digitsToReplace, int replaceWith
Restrictions: len(digitsToReplace) == #ofDigits(num), 0 <= replaceWith < 10
Returns: int """
def replaceDigits(num, digitsToReplace, replaceWith):
    newString = ""
    for i in range(len(str(num))):
        if digitsToReplace[i] == 1:
            newString += str(replaceWith)
        else:
            newString += str(num)[i]
    return int(newString)

""" Accepts a permutation list and an int. Builds a number in which the digits corresponding to a 1 in the
permutation are zeroes, and the others are the digits of the parameter int inserted in order.
Accepts: int insert, list<int> permutation
Restrictions: #ofDigits(insert) == len(permutation)
Returns: int """
def buildNum(insert, permutation):
    strInsert = str(insert)
    insertedSoFar = 0
    result = ""
    for i in range(len(permutation)):
        if permutation[i] == 1:
            result += "1"
        else:
            result += strInsert[insertedSoFar]
            insertedSoFar += 1
    return int(result)

def main():
    digits = MIN_DIGITS
    while True:
        permutationsSet = set()
        for i in range(1,digits):
            for perm in itertools.permutations([1] * i + [0] * (digits - i)):
                if perm[-1] != 1:
                    permCount = sum(perm)
                    for insertDigits in range(10**(digits - 1 - permCount),10**(digits - permCount)):
                        if insertDigits % 2 == 1:
                            numToReplace = buildNum(insertDigits, perm)
                            print(numToReplace)
                            primesFound = 0
                            for replace in range(10):
                                if replace != 0 or perm[0] != 1:
                                    newInt = replaceDigits(numToReplace, perm, replace)
                                    if isPrime(newInt):
                                        primesFound += 1
                                    if primesFound == NUM_PRIMES_DESIRED:
                                        for j in range(10):
                                            if isPrime(replaceDigits(numToReplace, perm, j)):
                                                print(replaceDigits(numToReplace, perm, j), perm)
                                                exit()
        digits += 1

if __name__ == "__main__":
    main()
"""    for j in range(10):
        print(replaceDigits(90007, [0,1,1,1,0], j), isPrime(replaceDigits(90007, [0,1,1,1,0], j)))"""