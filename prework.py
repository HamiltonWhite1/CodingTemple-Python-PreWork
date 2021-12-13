###Task 3 - Coding Questions


####Question 1
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as bellow.
def hello_name(user_name):
    return "hello_" + user_name.upper() + "!"
print(hello_name('Hamilton'))

####Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odds():
    num = 100
    for i in range(num):
        if i % 2 != 0:
            print(i)
print(first_odds())

####Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.
this_num_list = [23, 1, 4, 1, 44, 31]
def max_num_in_a_list(a_list):
    a_list.sort()
    return a_list[-1]
print(max_num_in_a_list(this_num_list))

####Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
# The return should be boolean Type (true/false).
def is_leap_year(year):
    leap = False
    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        leap = True
    
    if leap == True:
        return True
    
    if leap == False:
        return False
print(is_leap_year(2000))

####Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type.
another_num_list = [2,3,4,5,6]
def is_consecutive(a_list):
    is_it_consecutive = False
    current_num = 0
    previous_num = a_list[0]
    for i in a_list:
        current_num += i
        if current_num == a_list[0]:
            previous_num = i
            current_num = 0
            continue
        if current_num == previous_num + 1:
            previous_num = i
            current_num = 0
            is_it_consecutive = True
            continue
        else:
            is_it_consecutive = False
            break
    return is_it_consecutive
print(is_consecutive(another_num_list))
