"""
Lesson #2: Conditionals & Loops

"""

# Conditionals

# So we learned how to compare variables, but how do we act on those comparisons?

if True:
    print("Do something")
else:
    print("Do something else")

number = 1

# When there are more than 2 conditions you can do this:
if number == 1:
    print("1")
elif number == 2:
    print("2")
elif number == 3:
    print("3")
else:
    print(f"Number is {number}")

"""
EXERCISE
Write code which takes a test score and converts it to a letter grade from A to F
"""
grade = 'A'



##############################################
# Loops (for and while)

drugs = ["weed","coke","ket","shrooms","acid","addy"]
# Say i want to print out all the drugs. One way i could do it is like this
print(drugs[0])
print(drugs[1]) # etc.....
# there is an easier way to do this

for drug in drugs: # this is the easiest way to do for loops. A new variable: "drug" in this case represents each drug in the list
    print(drug)

# for some situations you may use a slightly different syntax

for i in range(0, len(drugs)):
    print(drugs[i])

# why use this?
# What if i want to print all numbers from 1 to 10?

for i in range(1, 11):
    print(i)
# remember the range(start, end) command from the last lesson


# while loops are kind of a combination of loops and if statements
num = 1
while(num < 5):
    print(num)
    num += 1

# Be careful with while loops
# while(a condition which is always true):
# This will cause python to crash

"""
EXERCISE 2
Add all the EVEN numbers in a list together
"""
list1 = [1,2,3,4,5,6] # should be 12






# FUNCTIONS
# Its kind of annoying when all the code runs at once. There's a way to fix this


def addNumbers(num1, num2): # any variables can be passed here.
    return num1 + num2 # return is used to end the function. Any code after return is triggered will be skipped

# the function will not run unless called
result = addNumbers(1,1)
print(result)


"""
EXERCISE 3
Write a function to calculate the area of a rectangle. Then use this function to add the areas of all the rectangles together.
The rectangles array contains rectangles formatted as [WIDTH, LENGTH]
"""
# 10, 15, 25, 0, 100
rectangles = [[10,1],[3,5],[5,5],[2,0],[25,4]] # should be 150


def calculateArea(rectangle):
    #.... rest of the code
    pass # delete pass (prevents error when the function is empty)


# some other code will be needed in addition to the function code.



"""
EXTRA CREDIT: Figuring out how to do things on your own. Use google to look up the documentation to solve these. I am too lazy to teach you.

Additional concepts:
1. f strings
2. string methods (such as .title())
3. maybe some other stuff... idk its extra credit, figure it out

"""

# USE THIS LIST FOR THE PROBLEMS
cities = ["new york", "san francisco","london","tokyo","barcelona","bangkok","lisbon","los angeles","toronto"]

# Exercise 1 - print out all of the cities in the array WITH proper capitalization. **HINT: use string.title()
print("----- Exercise 1 -----")



# Exercise 2 - print out all the cities that are not in the visited cities array
print("----- Exercise 2 -----")
visited_cities = ["new york","london","bangkok"]



# Exercise 3 - dictionaries. Print out what I think about london. Use bracket notation to select a specific entry in a dictionary. Ex: dictionary['entry']
print("----- Exercise 3 -----")
city_reviews = {"new york":"my favorite","london":"cool but rainy","tokyo":"i really want to go"}



# Exercise 4 - math. Print out the city I have not been to. You must determine this programatically. 
print("----- Exercise 4 -----")
city_visits = {"new york":55,"london":2,"tokyo":0,"lisbon":1}


# Exercise 5. Print out the city from `city_visits` I have visited the most. You must determine this programatically. This one is hard.
print("----- Exercise 5 -----")


# Exercise 6. Pretty printing with f strings. Use f string notation to print out: "I live in Willy B, New York". You must use the provided variables.
print("----- Exercise 6 -----")
city = "New York"
where_i_live = "Willy B"