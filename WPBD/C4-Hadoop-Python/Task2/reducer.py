import sys

curr_character = None
curr_count = 0

for line in sys.stdin:
    # Get tab-separated Key Value pairs
    character, count = line.split('\t')
    count = int(count)

    # If the current character is the same as the previous character,
    # increment its count
    # otherwise print the characters count to stdout
    if character == curr_character:
        curr_count += count
    else:
        if curr_character:
            print('{0}\t{1}'.format(curr_character, curr_count))
        
        curr_character = character
        curr_count = count

# Output the count for the last character
if curr_character == character:
    print('{0}\t{1}'.format(curr_character, curr_count))