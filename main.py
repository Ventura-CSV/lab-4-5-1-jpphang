import random


def main():
    """
    ########################################
    Code Your Program here
    ########################################
    """
    #initialize empty list
    numbers = []
    
    #generate 5 random numbers (0~100) to store in list
    count = 0
    while count < 5:
        random_nums = random.randint(0,101)
        numbers.append(random_nums)
        count = count + 1
    

    print(f'The random values are {numbers}')
    print(f'The total is {total}')

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()
