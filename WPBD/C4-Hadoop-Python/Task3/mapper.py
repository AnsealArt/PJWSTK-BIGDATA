import sys

for line in sys.stdin:
    numbers = line.split()

    for number in numbers:

        # Write tab-separated key-value pairs to stdout
        # Key is number, value is number of occurences
        print('{0}\t{1}'.format(int(number), 1))