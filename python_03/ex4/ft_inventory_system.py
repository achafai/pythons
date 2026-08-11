import sys

inputs: dict = dict(a.split(':') for a in sys.argv[1:])

print(inputs)
