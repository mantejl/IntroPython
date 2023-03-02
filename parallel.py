# NAME: Mantej Lamba
# ID: 2259394598
# DATE: 2022-09-28
# DESCRIPTION: practicing and working with altering strings and working with Lists

from typing import List


def stretch_string(s: str, stretch_factors: List[int]) -> str:
    # creating empty string
    str = ''
    # iterating through the given string
    for i in range(len(s)):
        # iterating through the List
        for j in range(stretch_factors[i]):
            # adding the character i many number of times to str
            str += s[i]
    # returning str
    return str


def greatest_difference(nums1: List[int], nums2: List[int]) -> int:
    # creating int value
    temp = 0
    # iterating through the first list
    for i in range(len(nums1)):
        # finding the absolute value difference between ith values in nums1 and nums2
        diff = abs(nums1[i] - nums2[i])
        # checking if the difference is greater than the temp value
        if diff > temp:
            # if it is, then assign it to the temp value
            temp = diff
    # returning max
    return temp


def main():
    # testing stretch string
    print(stretch_string('Hello', [2, 0, 3, 1, 1]))
    # testing stretch string
    print (stretch_string('echo', [0, 0, 1, 5]))
    # testing greatest difference
    print (greatest_difference([1, 2, 3], [6, 8, 10]))
    # testing greatest difference
    print (greatest_difference([1, -2, 3], [-6, 8, 10]))

if __name__ == "__main__":
    main()