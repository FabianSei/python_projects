"""A perfect number is a positive integer that is equal to the sum of its proper divisors.
A proper divisor of a positive integer is any divisor of other than itself. Thus, prime numbers have 
exactly one proper divisor, 1, and every other number has at least two proper divisors.
Write a program to get the maximal perfect number up to a given limit."""


def perfectNumber(a_limit):
    perfectNumbers = list()

    for number in range(1, a_limit):
        sum = 0
        for divisor in range(1, number):

            if number % divisor == 0 and number != divisor:
                sum += divisor

        if sum == number:
            pnum = sum
            print(pnum, " is a perfect number")
            perfectNumbers.append(pnum)
        else:
            pass

    return """The perfect numbers from 1 to %s are: %s.
The maximal perfect number from 1 to %s is: %s""" %(a_limit, perfectNumbers, a_limit, max(perfectNumbers))



print(perfectNumber(int(input("Chose a limit for perfect number: "))))
