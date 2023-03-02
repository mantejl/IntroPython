# Name: Mantej Lamba
# ID: 2259394598
# Date: 2022-09-26
# Description: working with lists and changing their values to match the instructions

from typing import List

def collect_below_threshold(nums: List[int], threshold: int) -> List[int]:
    # creating an list to hold the appropriate values from num
    list = []
    # for loop to iterate through nums
    for i in nums:
        # checking if the element is less than the threshold
        if i < threshold:
            # if it is, then we add it to the declared list written in line 10
            list.append(i)

    # returning the new list with the appropriate values
    return list

def scale_midterm_grades(grades: List[int], multiplier: int, bonus: int) -> None:
    # iterating through the grades list to access and change each value
    for i in range(0,len(grades)):
        # multiplying each value in grades by the multiplier value
        grades[i] = grades[i] * multiplier
        # adding each value in grades with the bonus value
        grades[i] = grades[i] + bonus
        # checking if each value in grades is greater than 100
        if grades[i] > 100:
            # if it is, then we cap it at 100 to match the instructions
            grades[i] = 100



# Complete the following
def main():
    # creating our first list with values
    first = [1,2,3,4]
    # calling the threshold method and assigning a list variable to store it
    firstList = collect_below_threshold(first, 3)
    # iterating through the first list and printing out the values on 1 line
    for i in firstList:
        print (i, end = " ")
    # adding the extra print statement to move to the next line
    print()
    # creating our second list with values
    second = [1, 2, 108, 3, 4]
    # calling the threshold method and assigning a list variable to store it
    secondList = collect_below_threshold(second, 50)
    # iterating through the second list and printing out the values on 1 line
    for i in secondList:
        print (i, end = " ")
    # adding the extra print statement to move to the next line
    print()
    # creating our third list
    third = []
    # calling the threshold method and assigning a list variable to store it
    thirdList = collect_below_threshold(third, 7)
    # iterating through the second list and printing out the values on 1 line
    for i in thirdList:
        print (i, end = " ")
    # adding the extra print statement to move to the next line
    print()
    # creating our grades list with values
    grades = [45, 50, 55, 95]
    # calling the scale method to alter the values in grades
    scale_midterm_grades(grades, 1, 10)
    # iterating through the grades list and printing out the values on 1 line
    for i in grades:
        print (i, end = " ")

if __name__ == "__main__":
    main()

