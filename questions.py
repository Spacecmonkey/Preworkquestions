

# Question number 1 
def hello_name(user_name):
    print(f"hello_{user_name}!")
hello_name("Brolin")


#  Question number 2 
def first_odds():
    for number in range(1, 101 ,2):
        print(number)
first_odds()

# Question 3 
def max_num_in_list(a_list):
    return max(a_list, default=None)
numbers = [1, 4, 6, 8, 17, 22]
print(max_num_in_list(numbers))

# Question 4 
def is_leap_year(a_year):
    if a_year % 4 == 0:
        if a_year % 100 ==0:
            return a_year % 400 == 0
        else:
            return True
    else:
        return False
year = 2024
result = is_leap_year(year)
print(f"Is {year} a leap year? {result}")

# Question 5 
def is_consecutive(a_list):
    if len(a_list) < 2:
        return True  

    
   
    sorted_list = sorted(a_list)
    
   
    for i in range(1, len(sorted_list)):
        if sorted_list[i] - sorted_list[i-1] != 1:
            return False
    
    return True


list1 = [2, 3, 4, 5, 6, 7]
list2 = [1, 2, 4, 5]

result1 = is_consecutive(list1)
result2 = is_consecutive(list2)

print(f"Is list1 consecutive? {result1}")
print(f"Is list2 consecutive? {result2}")
