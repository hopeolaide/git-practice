# Taken From
# Iterating Over Data
# Problem-Set While Loops #11
def silly_sum():
    """ reads numbers from the user (use input_int) 
        summing as we go until either
        the user enters 0, or
        the sum reaches or exceeds 1000
    """
    silly_sum = 0
    user_number = input_int("Enter a number: ")
    user_number_list = []
    while silly_sum < 1000:
        if user_number != 0:
            user_number_list.append(user_number)
            for number in user_number_list:
                silly_sum += number
    
    return silly_sum

def input_int(*args):
    # loop forever (until we get valid input)
    while True:
        # get string input
        user_input = input(*args)
        try:
            # try converting to an int (will return if successful)
            return int(user_input)

            # if the conversion succeeded, we will have returned already
        except ValueError:
            # could not convert the input, so show an error message
            print('Try again.')




if __name__ == "__main__":
    print(f"Answer = {silly_sum()}")
