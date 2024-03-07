"""
Sean Killian
Thursday @ 2pm
"""

def filter_and_print_range(input_list, min_val, max_val):
    #write your code here
    integer_list = list(map(int, input_list.split()))

    for num in integer_list:
        if min_val <= num <= max_val:
            print(num, end=",")

if __name__ == '__main__':
    # Get input for the list of integers
    user_input_list = input("Enter a space-separated string of numbers: ")

    # Get input for the range (min and max values)
    min_val, max_val = map(int, input("Enter the min and max values separated by a space: ").split())

    # Call the function to filter and print the numbers in the given range
    filter_and_print_range(user_input_list, min_val, max_val)
