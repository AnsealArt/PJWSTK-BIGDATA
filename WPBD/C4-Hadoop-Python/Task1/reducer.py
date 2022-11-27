import sys

curr_word = None
curr_count = 0

for line in sys.stdin:
    # Get tab-separated Key Value pairs
    word, count = line.split('\t')
    count = int(count)

    # If the current word is the same as the previous word,
    # increment its count
    # otherwise print the words count to stdout
    if word == curr_word:
        curr_count += count
    else:
        if curr_word:
            print('{0}\t{1}'.format(curr_word, curr_count))
        
        curr_word = word
        curr_count = count

# Output the count for the last word
if curr_word == word:
    print('{0}\t{1}'.format(curr_word, curr_count))