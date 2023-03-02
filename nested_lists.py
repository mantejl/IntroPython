# NAME: Mantej Lamba
# ID: 2259394598
# DATE: 2022-10-03
# DESCRIPTION: practicing and working with altering strings and working with Lists

from typing import List


def digital_sum(nums_list: List[str]) -> int:
    # creating variable total = 0
    total = 0
    # iterating through nums_list
    for i in nums_list:
        # iterating through each digit in each element in the list
        for number in str(i):
            # adding each digit to the total sum
            total += int(number)

    # returning the total
    return total



def can_pay_with_two_coins(denoms: List[int], amount: int) -> bool:
    # iterating through the list
    for one in range (len(denoms)):
        # iterating through the list again
        for two in range(one, len(denoms)):
            # adding the first value to all the rest and checking if they equal the amount
            if(denoms[one]+denoms[two] == amount):
                # if it does then we return True
                return True

    # returning False otherwise
    return False


def main():
    # test cases for digital sum function
    print(digital_sum(['64', '128', '256']))
    print(digital_sum(['12', '3']))
    # test cases for can pay with two coins function
    print(can_pay_with_two_coins([1, 5, 10, 25], 35))
    print(can_pay_with_two_coins([1, 5, 10, 25], 20))
    print(can_pay_with_two_coins([1, 5, 10, 25], 12))



if __name__ == "__main__":
    main()
