# Hello James, your first homework for today is to create a python function can given a parameter
# return True, if the parameter is even and False if the parameter is odd.


# Hi James, I like this work but I want you to make the following changes:
# - I want the function to keep asking the user for numbers until the user types 'q'
def is_even(x):
    if x % 2 == 0:
        print(True)
    else:
        print(False)


def main():
    while True:
        x = input("Enter a number of choice:")
        if x == 'q':
            break
        is_even(int(x))



main()