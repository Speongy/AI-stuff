'''
Kevin Nguyen
2022_Fall_CPSC_4370_48F_1 - Artificial Intelligence
Kockara
'''
# #TODO Hello World Example
# for i in range(10):
#     print('Hello')

# #TODO User Input
# name = 'kevin'
# print('Hello ' + name)

# print('Enter your name: ')
# x = input() #! gets input from keyboard
# print('Hello, ' + x)

# #TODO Equations
# import math
# print((((1+2)*3)/4)**5)
# print(9%4) #!remainder
# print(5//2) #!integer divider
# print(9**(1/2)) #!sqrt(9)
# print(27**(1/3)) #! 3rd root(9)
# print(math.pow(9, 1/2))
# print(math.sqrt(9))
# print(math.sin(math.pi/2))

# print('\n')

# #TODO Data Types
# num = 7
# name = 'kevin'
# f1Number = 1.234
# print(type(num))
# print(type(name))
# print(type(f1Number))
# print(int(f1Number))
# print(f1Number + num)

# #TODO Variables
# import math
# pii = math.pi
# print(type(pii))
# print(pii)
# radius = 4.5
# area = pii * (radius**2)    
# print("Area of a circle of radius " + str(radius) + " equals: " + str(area))

# print("\n")

# #TODO Functions
# def circleArea(radius):
#     return math.pi*radius**2
# radius = 4.5
# print(circleArea(radius))

# print("\n")

# def get_seconds(hours = 0, min = 0, sec = 0):
#     print(sec)
#     return 3600*hours + 60*min + sec
# amountA = get_seconds(2, 30)
# amountB = get_seconds(sec=15)

# result = amountA + amountB
# print(result)

# def convert_seconds(seconds):
#     hours = seconds
#     minutes = (seconds - hours*3600)//60
#     remaining_seconds = seconds - hours * 3600 - minutes*60
#     return hours, minutes, remaining_seconds
# hours, minutes, seconds = convert_seconds(7385)
# print("hours: " + str(hours) + ", " + "minutes: " + str(minutes) + ", seconds: " + str(seconds))

# #TODO Comparison Operators
# print(10>9)#prints  True
# print(10<9)#prints False
# print("apple" == "apples")#equal operator, prints False
# print(10 != 9)#not equal operator, prints True
# print( 1 ==  "1")#equality operator, prints False
# print()
# print("cat" > "Cat")#greater operator, prints True
# print("cat" >= "Cat")#greater or equal operator, prints True
# print("cat" < "Cat")#smaller operator, prints False
# print("cat"  >  "Cat" and "dog" > "Dog")#logical and operator, prints True
# print("cat" >= "Cat")#greater or equal operator, prints True
# print()
# print(25>25 or 1 !=5)#logical or  operator, prints True
# print(not(25>25 or 1 !=5))#not operator, prints False

# #TODO Conditionals
# def hintUsername(username):
#     length=len(username)
#     if  length<3: # len() is builtin function, returns length of a given argument
#         print("Username must consist of at least 3 characters. Yours is: "+str(length))
#     elif length > 15:
#         print("Invalid user name. User name cannot be more than 14 characters")
#     else:
#         print(username + " is a valid user name!")
# print("Username:")

# username=input()
# hintUsername(username)

# def isEven(number):
#     if number % 2 ==0:
#         return True
#     return False
# print("20 is an even number:  "+str(isEven(20)))

# #TODO Loops
# x = 0
# while x<5:
#     print("Not there yet, x = "+str(x))
#     x = x+1
# print("x = "+str(x))

# def attempts(n):
#     x = 1
#     while x <= n:
#         print("Attempt " + str(x))
#         x += 1 #same as x = x+1
#     print("Done")
# attempts(5)

# def get_username(maxnumber_of_tries):
#     print("Enter  your username")
#     username = input()
#     while not valid_username(username):
#         maxnumber_of_tries -= 1
#         #print('maxnumber_of_tries = ' +str(maxnumber_of_tries))
#         if maxnumber_of_tries == 0:
#             print('Reached to maximum trials!')
#             break
#         print('Invalid user name')
#         username = get_username(maxnumber_of_tries)#recursive call
#     return username

# def valid_username(username):
#     if not username.isalpha():
#         reason = 'Username can only contain alphabetical characters'
#         print(reason)
#         return False
#     if len(username) < 8:
#         reason = 'Must have at least 8 alphabetical characters'
#         print(reason)
#         return False
#     if not any(x.isupper() for x in username): #simply checking if any of the chars in username is upper case, then returns True
#         reason = 'Username must contain at least one uppercase character'
#         print(reason)
#         return False
#     print('User name is good!')
#     return True

# username = get_username(2)
# print()
# print(valid_username('ThisWorks'))#prints True
# print(valid_username('This_Fails'))#prints False
# print(valid_username('thisfails'))#prints False
# print(valid_username('fails'))#prints False

# def square(n):
#     return n*n

# def sum_squares(x):
#     sum = 0
#     for n in range(x): #range() function starts from 0
#         sum += square(n)
#     return sum

# print(sum_squares(10)) # Should be 285

# friends = ['John','Barbara','Amy','Eli','Barbara',5]#list data structure, allows duplicates
# for friend in friends:
#     if type(friend) == 'str':
#         print('Hi '+friend)
#     elif type(friend) ==  int:
#         print('Hi int number '+str(friend))
# print()
# for index in range(3,len(friends)):#now range starts at 3 to 6 (length  of the friends list)
#     print(friends[index])# can directly access list elements with an index, array notation

# print()#to print an empty line
# print(friends[0])
# print(str(friends[5]))
# friends[5] = 'Eli' #list is a mutable data structure; its value can change

# print(friends[5])
# print('length of list friends is: '+str(len(friends)))

# def factorial(n):
#     result = 1
#     for i in range(1,n+1):
#         #print(i)
#         result *= i
#     return result

# print(factorial(4)) # should return 24
# print(factorial(5)) # should return 120

# #recursive factorial, easier to understand comparing to the previous version
# #recursive functions in Python can be called upto 1,000 times!
# def rec_factorial(n):
#     if n < 2:
#         return 1
#     return n*factorial(n-1)
# print("Recursive factorial:")
# print(rec_factorial(4)) # should return 24
# print(rec_factorial(5)) # should return 120
# def sum_positive_numbers(n):
#   if n == 1:
#     return 1
#   return n+sum_positive_numbers(n-1)

# print(sum_positive_numbers(3)) # Should be 6
# print(sum_positive_numbers(5)) # Should be 15

# def to_celcius(temp_in_fahrenheit):
#     return(temp_in_fahrenheit-32)*5/9
# for temprature in range(0,101,10): # 3rd argument in range  determines #increments. range takes 1, 2 ,or 3 parameters.
#     print(temprature, to_celcius(temprature))

# def to_formatted_celcius(temp_in_fahrenheit):
#     return(temp_in_fahrenheit-32)*5/9
# for temprature in range(0,101,10): # 3rd argument in range  determines increments.
#     print('{:>3} F| {:>6.2f} C'.format(temprature, to_formatted_celcius(temprature)))
#     #{:>3} aligns to the right with 3 spaces, {:>6.2f} aligns to the right with 6 spaces and 2 digits for fractions
# for left in range(7): #domino tiles’ values  from 0 to 6
#     for right in range(left,7):
#         print('['+str(left)+'|'+str(right)+']', end = ' ')#by default print() #outs newline characted to the end
#         #here end is specified as a space; thus there will be space at the 
# #end  of each print.
#     print()#newline  put  after inner loop  is completed

#TODO Strings
message = "Example"
print(3*message) #prints ExampleExampleExample
print(len(3*message))#prints 21
print(message[3])#prints m, index starts at zero
print(message[len(message)-1])#prints last element 'e', -1 is because index starts at 0
print(message[-1])#Negative index refers from the tail; prints the last indexed element 'e'
print(message[-2])#prints the one before the last indexed element
print(message[1:4])#Slicing example, [1,4): left index 1 included, right index 4 excluded.
print(message[:5])#prints Examp
print(message[2:])#prints ample
print(message[::2])#increments index by 2 starting from 0 indexed one; 'Eape', prints every other character
#message[0] = 'e' # will generate an error: 'str' object does not support item assignment.
#the way of getting around this is as follows
newmessage = 'e'+message[1:]
print(newmessage)
#however, you can assign a whole new value to an existing string. see below example
message = 'Cats & Dogs'
print(message)#prints Cats & Dogs
print(message.index('&')) #prints index of '&' in message
print(message.index('Dog'))#prints where 'Dog' firs occur in the string, starting index
print(message.index('s'))#prints the first occurance index of 's'
#print(message.index('S')) # generates error or won't run because 'S' does not exist in message
print('Cats' in message)#prints True because 'Cats' exists in the message
print('snake' in message)#prints False
print(message.count('s'))#prints 2 on screen because 's' exists 2 times in message
print(message.count('Cats'))#prints 1
print(message.endswith('Dogs'))#prints True
print('1234'.isnumeric())#prints True
print(int("3456")+int('153'))#prints 3609
print('#'.join(['This','class','is','fun','if','there','was','no','#']))
listofstrings = 'This class is fun!'.split()#split returns a list of strings
print(listofstrings)
print(listofstrings[2])#prints 'is'

newstring='bicycle'.upper()#makes all upper case
print(newstring)

newstring = newstring.lower()#makes all lower case
print(newstring)

print("Enter Yes or No")
answer = input()
if answer.lower() == 'yes':
    print("your answer is:", answer)
print()
print(' yes  '.strip())#removes whitespaces in both left and rigt ends, prints 'yes'
print(' yes  '.lstrip()) #prints 'yes  '
print(' yes  '.rstrip()) #prints ' yes'
print()

name='Kevin'
number = len(name)*3
print('Hello {}, your lucky number is {}!'.format(name,number))#format() populates {} with variables
print('Hello {name}, your lucky number is {number}!'.format(name=name,number= len(name)*2))#prints Hello Sinan, your lucky number is 10!
price=253.98
with_tax=price*1.09
print(price, with_tax)
#let's format it so that on prints 2 digits after point.
print('Base price is ${:.2f}. With tax, total price is ${:.2f}'.format(price,with_tax))

first = "apple"
second = "banana"
third = "carrot"
formatted_string = "{0} {2} {1}".format(first, second, third)
print(formatted_string)#prints apple carrot banana
print('snake' in message)#prints False

def first_and_last(message):
    if message == '':
        print("Empty string", end=',')
        return True
    elif message[0]==message[-1]:
        return True
    else:
        return False

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))


#example of changing old domain email to new domain
def replace_domain(email, old_domain, new_domain):
    if '@'+old_domain in email:
        index = email.index('@'+old_domain)
        new_email = email[:index]+'@'+new_domain
        return new_email
    return email

email  = 'knguyen24@something.edu'
email = replace_domain(email, 'something.edu','lamar.edu')
print(email)#changes from ol_domain to new_domain


def abbreviate(phrase):
    wordslist = phrase.split()
    result = ""
    for word in wordslist:
        result += word[0].upper()
    return result
print(abbreviate("Universal Serial Bus")) # Prints USB
print(abbreviate("local area network")) # Prints LAN
print(abbreviate("Operating system")) # Prints OS


def student_grade(name, grade):
   return "{} received {}% on the exam".format(name,grade)
print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))


def is_palindrome(input_string):
   new_string = ''.join(input_string.split()).lower()
   reverse_string =new_string[::-1]
   if reverse_string ==  new_string:
      return True
   else:
      return False
print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True


def convert_distance(miles):
   km = miles * 1.6 
   result = "{} miles equals {:.1f} km".format(miles,km)
   return result
print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km


def nametag(first_name, last_name):
   return("{} {}.".format(first_name,last_name[0].upper()))
print(nametag("Jane", "Smith")) 
# Should display "Jane S." 
print(nametag("Francesco", "Rinaldi")) 
# Should display "Francesco R." 
print(nametag("Jean-Luc", "Grand-Pierre")) 
# Should display "Jean-Luc G."


#only replaces old with new if old is at the end of the sentence
def replace_ending(sentence, old, new):
    # Check if the old string is at the end of the sentence
    index = sentence.rfind(old)
    if index == len(sentence) - len(old):
        # Using index as the slicing index, combine the part
        # of the sentence up to the matched string at the
        # end with the new string
        new_sentence = sentence[:index] + new
        return new_sentence
    # Return the original sentence if there is no match
    return sentence

print(replace_ending("It's raining cats and cats", "cats", "dogs"))
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts"))
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april"))
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April"))

#TODO List Data Structure
list = ["now",1, "is",2,"good time"]#having different types in list is ok!
print(type(list))#prints <class 'list'>
print(len(list))#prints 5
print("good time" in list)#prints True
print(list[0])#accessing indexed element
print(list[1:3])#slicing is ok. prints [1, 'is']
list2=["here",'we',"go"]
print(list+list2)
print(list)
list.append(list2)#appends list2 into list
print(list)#prints ['now', 1, 'is', 2, 'good time', ['here', 'we', 'go']] Notice that last element is  a list
#therefore its  length is 6  (not 8) as 6th element being another list
print(len(list))#prints 6
list.append("JOHN")
print(list)
list.insert(7,'JOHNNY')#inserts JOHNNY in index position 7
print(list)
list.insert(12,"AMY")#No error. if given index is larger than the len(list) AMY will be appended
print(list)
list.remove(1)#removes 1 from the list
print(list)
print("REMOVING")

for i in list:
    print(i)
    if isinstance(i, type(list)):#if instance in list variable's type is a #list type, remove it from the list variable
        list.remove(i)
print(list)
print(list.pop(2))#pops index 2 element from list and returns that element
print(list)
list[2] = "Barbara" #changes 3rd element in list from 'good time' to 'Barbara'
print(list)

animals = ['Crocodile','Cheetah','Rhino','Zebra','Lion']
animals.sort()# sorts list
print(animals)#prints sorted list

numtotalchars = 0
for animal in animals:
    numtotalchars += len(animal)
print("total chars in list is {}, Average length of animal name is {}".format(numtotalchars,numtotalchars/len(animals)))

def get_word(sentence, n):
    words = sentence.split()
    if n > 0:
        # Only proceed if n is not more than the number of words
        if n <= len(words):
            return(words[n-1])
    elif n<0 & abs(n)<=len(words):
        return (words[n])
    else:
        return("")
print(get_word("This is a lesson about lists", 4)) #prints lesson
print(get_word("This is a lesson about lists", -4)) # prints 'a'
print(get_word("Now we are cooking!", 1)) # prints 'Now'
print(get_word("Now we are cooking!", 5)) #prints 'None'

def skip_elements(elements):
# Initialize variables
    new_list = elements[::2]
    return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []

#this time with enumerate() function
def skip_elements(elements):
    newlist  = []
    for index, element in enumerate(elements):
        if index % 2 == 0:
            newlist.append(element)
    return newlist

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']

#List Comprehension example
multiplesof9=[]
for x in range(1,13):
    multiplesof9.append(9*x)
print(multiplesof9)
#doing the same thing with List Comprehension
multiplesof9 = [x*9 for x in range(1,13)]
print(multiplesof9)

#another example
languages = ['Python','C/C++','Java', 'Ruby','Pascal','Perl','Lisp','Prolog']
lengthslist =[len(language) for language in languages]
print(lengthslist)

#another example
multiplesof3 = [ i for i in range(1,100) if i%3 ==0]
print(multiplesof3)#prints multiples of 3

#List Comprehension 
def odd_numbers(n):
   return [x for x in range(n+1) if x % 2 != 0]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []

files = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
print(files)
def change_hpp_to_h(files):
    #newfilenames=[]
    for i,file in enumerate(files):
        if file[file.index('.'):] == '.hpp':#if after  '.' file extension is #'hpp'
        	files[i] = file[:file.index('.')]+'.h'
        else:
            files[i] = file
    return files

print(change_hpp_to_h(files))
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

def group_list(group, users):
  members = ','.join(users)
  return group+':'+members

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"


#TODO Tuple Data Structure
def file_size(file_info):
   filename, filetype, filesize= file_info
   return("{:.2f} KB".format(filesize / 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21

def emails_and_owners(people):
    #tuple will consist of email and name pairs
    result = [] #a list of tuples will be returned
    for email,person in people:
        result.append('{} <{}>'.format(email,person))
    return result
print(emails_and_owners([("skockara@lamar.edu", "Sinan Kockara"),("alexdesouza@gmail.com","Alex  R. DeSouza")]))

def guest_list(guests):
   for guest in guests:
      print('{} is {} years old and works as {}.'.format(guest[0],guest[1],guest[2]))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

#TODO Dictionaries
#Dictionary: each key only occurs once!

x={}
print(type(x))#prints <class 'dict'>
file_counts = {'jpeg':11, 'txt':13, 'docx':21,'csv':45,  'py':131}
print(file_counts)
print(file_counts['txt'])#prints value 13 for key 'txt'
print('jpeg' in file_counts)#prints True
print('html' in file_counts)#prints False
file_counts['csv']+=10  #dictionary is mutable
print(file_counts)#'csv' key's value became 55
del file_counts['csv']#deletes 'csv':55 pair from dictionary
print(file_counts)
file_counts['html'] = 3 #adds new element if key 'html' does not exist
print(file_counts)

#iterating over dictionary keys
for extension in file_counts:
    print(extension)#prints all keys

#if we  need to access both key and values, then use items() method to get a tuple of key, value pairs
for extension, num in file_counts.items():
    print('there are {} files with the .{} extension'.format(num, extension))

print(file_counts.keys())#prints all the keys returned as a list of keys
print(file_counts.values())#prints all the values returned a list of values
for value in file_counts.values():
    print(value)#prints each value of the dictionary

cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}

print(sorted(cool_beasts.items()))#sorted sorts the dictionary by keys and returns a list of tuples not dictionary
print(cool_beasts)
cool_beasts = dict(sorted(cool_beasts.items())) #items()  needed to do sorting for key value pairs
print(cool_beasts)#now prints sorted dictionary
for key,value in cool_beasts.items():
    print("{} have {}".format(key,value))

def count_letter(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result
print(count_letter('Here we go! We are now counting frequency of letters in this very sentence!'))

wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for key, values in wardrobe.items():
   for value in values:
      print("{} {}".format(value, key))

def email_list(domains):
    emails = []
    for domain,users in domains.items():#domain is key, users is value
        for user in users:
            emails.append(user+'@'+domain)
    return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))

def add_prices(basket):
   # Initialize the variable that will be used for the calculation
   total = 0
   # Iterate through the dictionary items
   for item, value in basket.items():
      total += value
   # Limit the return value to 2 decimal places
   return round(total, 2)

groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59,
   "coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries)) # Should print 28.44

#TODO Set
# Different types of sets in Python
# set of integers
my_set = {1, 2, 3}
print(my_set)

# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)

# set cannot have duplicates
# Output: {1, 2, 3, 4}
my_set = {1, 2, 3, 4, 3, 2}
print(my_set)

# we can make set from a list
# Output: {1, 2, 3}
my_set = set([1, 2, 3, 2])
print(my_set)

# set cannot have mutable items
# here [3, 4] is a mutable list
# this will cause an error.

#my_set = {1, 2, [3, 4]}# this line generates error message: 'TypeError: unhashable type: 'list''

# Distinguish set and dictionary while creating empty set

# initialize a with {}
a = {}

# check data type of a
print(type(a))#prints <class 'dict'>

# initialize a with set()
a = set()

# check data type of a
print(type(a))#prints <class 'set'>
# initialize my_set
my_set = {1, 3}
print(my_set)

# my_set[0]
# if you uncomment the above line
# you will get an error
# TypeError: 'set' object does not support indexing

# add an element
# Output: {1, 2, 3}
my_set.add(2)
print(my_set)

# add multiple elements
# Output: {1, 2, 3, 4}
my_set.update([2, 3, 4])
print(my_set)

# add list and set
# Output: {1, 2, 3, 4, 5, 6, 8}
my_set.update([4, 5], {1, 6, 8})
print(my_set)

# Difference between discard() and remove()

# initialize my_set
my_set = {1, 3, 4, 5, 6}
print(my_set)

# discard an element
# Output: {1, 3, 5, 6}
my_set.discard(4)
print(my_set)

# remove an element
# Output: {1, 3, 5}
my_set.remove(6)
print(my_set)

# discard an element
# not present in my_set
# Output: {1, 3, 5}
my_set.discard(2)
print(my_set)

# remove an element
# not present in my_set
# you will get an error.
# Output: KeyError

#my_set.remove(2) # this line will generate error message
# initialize my_set
# Output: set of unique elements
my_set = set("HelloWorld")
print(my_set)#prints {'H', 'l', 'r', 'W', 'o', 'd', 'e'}

# pop an element
# Output: random element

print(my_set.pop())#pops a random element from set, in my case that was 'l'

# pop another element
my_set.pop()
print(my_set)

# clear my_set
# Output: set()
my_set.clear()
print(my_set)
# Set union method
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use | operator
print(A | B)#Union operation, or A.union(B) = B.union(A), prints {1, 2, 3, 4, 5, 6, 7, 8}
# Intersection of sets
# use & operator
# Output: {4, 5}
print(A & B)#or A.intersection(B) = B.intersection(A)
# Difference of two sets
# Output: {1, 2, 3}
print(A - B)# A-B != B-A
# use ^ operator for symmetric difference
# Output: {1, 2, 3, 6, 7, 8}
print(A ^ B)# or A.symmetric_difference(B) =  B.symmetric_difference(A)
print(1 in A)#prints True



