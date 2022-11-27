import sys
import statistics

# Global variables
processed_numbers = 0
curr_max_value = -sys.maxsize - 1
curr_arith_avg = 0
curr_geo_avg = 0
curr_median = 0
unique_numbers = set()
all_numbers = list()
product_of_all_numbers = 1

def calculate_stats(incoming_number):

    global processed_numbers
    global curr_max_value
    global curr_arith_avg
    global curr_geo_avg
    global curr_median
    global unique_numbers
    global product_of_all_numbers

    processed_numbers += 1
    all_numbers.append(incoming_number)

    # Max Value
    if curr_max_value < incoming_number:
        curr_max_value = incoming_number

    # Arithmetic Average
    curr_arith_avg = sum(all_numbers) / processed_numbers

    # Geometric Average
    product_of_all_numbers *= incoming_number
    curr_geo_avg = product_of_all_numbers ** (1 / processed_numbers)

    # Median
    curr_median = statistics.median(all_numbers)

    # Unique Number
    unique_numbers.add(incoming_number)

def print_stats():
    print('Max value is: {0}'.format(int(curr_max_value)))
    print('Arithmetic Average: {0}'.format(curr_arith_avg))
    print('Geometric Average is: {0}'.format(curr_geo_avg))
    print('Median is: {0}'.format(curr_median))
    print('Number of unique values is: {0}'.format(len(unique_numbers)))
    print('Total number of values is: {0}'.format(len(all_numbers)))


for line in sys.stdin:
    # Get tab-separated Key Value pairs
    number, count = line.split('\t')
    count = int(count)
    number = float(number)

    # Update statistics based on currently processed number
    calculate_stats(number)

print_stats()