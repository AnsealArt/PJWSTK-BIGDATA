import sys

for line in sys.stdin:
    words = line.split()

    for word in words:
        characters = list(word)

        for character in characters:
            # Write tab-separated key-value pairs to stdout
            print('{0}\t{1}'.format(character, 1))