#!/usr/bin/python3
import sys
import time

factorize = __import__("factors").factorize

"""
Read the number in file
"""
if len(sys.argv) != 2:
    print("Usage: factors <file>")
    exit()

filename = sys.argv[1]

try:
    with open(filename, "r") as file:
        lines = file.readlines()
except FileNotFoundError:
    raise FileNotFoundError("Error: file not found")
    exit()

start_time = time.time()
"""
Loop over each line in the file which contains a natural number
call factorize def for each number
"""
for line in lines:
    number = int(line.strip())
    factors = factorize(number)
    if factors:
        print("{:d} = {:d} * {:d}".format(number, factors[0], factors[1]))

"""
If excute of the program pass 5 seconds,
the program exit with an error message
"""
if time.time() - start_time > 5:
    raise TimeoutError("Error: Time limit exceeded")
    exit()
