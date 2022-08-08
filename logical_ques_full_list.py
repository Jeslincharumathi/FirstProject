# """-------------------------------------------------Reverse_the_list----------------------------------"""

list_1 = [5,4,3,2,1]
print(list_1[::-1])
result = list_1
print(result)

for i in range(0,100):
    print(i)

# # ------------------------------------------------------------------------------------------------------

# """---------------------------------------------------Pallindrome----------------------------------"""

input = "madam" 
output = "madam"

input = "jeslin"
output = "nilsej"


word = "madams"
rev = ""

def rev_str(str):
    rev_str1 = ""        
    for i in str:
        rev_str1 = i + rev_str1
    return rev_str1

str = "jeslin"
print(rev_str(str))


# # ------------------------------------------------------------------------------------------------------

# """--------------------------------------Check number is positive or negative----------------------------------"""

# #Python Program to Check if a Number is Positive, Negative or 0
num = float(input("Enter a number: "))
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")


# #Python Program to Check if a Number is Odd or Even

num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))


# # ------------------------------------------------------------------------------------------------------

# """--------------------------------------------------Prime number----------------------------------"""


# # # # # Python Program to Check Prime Number
num = 29

flag = False

if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")

# # ------------------------------------------------------------------------------------------------------

# """----------------------------------------------   Fibonacci    ----------------------------------"""


nterms = int(input("How many terms? "))
n1, n2 = 0, 1
count = 0
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1
# # ------------------------------------------------------------------------------------------------------

# """-----------------------------------------   Function  ----------------------------------"""


def calculation(a, b):
    res = calculation(40, 10)
    print(res)

# # ------------------------------------------------------------------------------------------------------

# """------------------------------------------  Pallindrome  ----------------------------------"""


word = "madam"
emp_str = " "
for i in word:
    emp_str = i + emp_str
    if emp_str == word:
        print("palindrome")
    else:
        print("not pal")        
print(emp_str)

# # ------------------------------------------------------------------------------------------------------

# #Method-2

def pallindrome(str):
    rev_str = " "
    for i in str:
        rev_str = i + rev_str

    if rev_str == str:
        return "Pallindrome"
    else:
        return "Not a pallindrome"

str = "madam"
x = pallindrome(str)
print(x)

# #--------------------------------------------------------------------------------------------------

# # Method-3

def isPalindrome(str):
     
    # Run loop from 0 to len/2
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True

# #--------------------------------------------------------------------------------------------------
 
# # Method-4

s = "malayalam"
ans = isPalindrome(s)
 
if (ans):
    print("Palindrome")
else:
    print("Not Palindrome")
def isPalindrome(s):
     
    # Using predefined function to
    # reverse to string print(s)
    rev = ''.join(reversed(s))
 
    # Checking if both string are
    # equal or not
    if (s == rev):
        return True
    return False
 
# # ------------------------------------------------------------------------------------------------------

# """----------------------------------Repeating certain character in a string----------------------------------"""


s = {'a':1, 'b':2, 'c':1}
print(s.items())

a = "sachin"                
#output = "viiewiinsachiin"
b = ""
for char in a:              
    if char == "i":
        b += char + char
    else:
        b = b + char
print(b)

def x(str):
    res = ""
    for char in str:
         if char == "i":
            res += char + char
    return res

# # print(x("sachin"))

# # ------------------------------------------------------------------------------------------------------

# """--------------------------------------------------Prime number----------------------------------"""

# #M Example - 2

str_1="viewinsachin"
out=''
for i in str_1:
  if i == 'i':
    out = out +  i + 'i'
  else:
    out = out +i
print(out)

# # ------------------------------------------------------------------------------------------------------

# """---------------------------------------Dictionary key and its value----------------------------------"""

list_1 = ["jeslin", "charu", "mathi"]
list_2 = [1,2,3]
list_dict = dict(zip(list_1,list_2))
print(list_dict)
res = {}
for i in range(len(list_1)):
    res[list_1[i]] = list_2[i]
print(res)


# # ------------------------------------------------------------------------------------------------------

# """------------------------------------Frequency of a word in a string----------------------------------"""


str_1 = "john went to the market john is in office john is in home  "
sp_str = str_1.split()
# print("splitted sting be:",sp_str)
emp_str = {}
for i in sp_str:
    if i in emp_str:
        emp_str[i] = emp_str[i] + 1
    else:
        emp_str[i] = 1
print("Each word in str with its frequency:\n", emp_str)
# from this dict get the high frequency word:
max_value = None 
for key in emp_str:
    if max_value is None or max_value < emp_str[key]:
        max_value = emp_str[key]
        max_key =  key 
print("Heighest frequency of key is",max_key,"and value is", max_value)

# # ------------------------------------------------------------------------------------------------------

# """-----------------------------  Removing vowels and reverse the string  ------------------------------"""

# # print reverse string after removing vowels
# input = "duck"
# output = "kcd"
# word = "duck"
v = ['a','e','i','o','u']
emp = ""
for i in word:
    if i not in v:
        emp = emp + i
print("String without reversing after removing vowels:\n",emp)
# reverse the string we got
rev_str = ""
for i in emp:
    rev_str = i + rev_str
print("String after reversing:\n",rev_str)

# # ------------------------------------------------------------------------------------------------------

# """------------------------------------Removing vowels and reversing----------------------------------"""

# # input = "jeslin"
# # output = "nlsj"
word = "jeslin"
v = ['a','e','i','o','u']
emp = ""
for i in word:
    if i not in v:
        emp = emp + i
print("String without reversing after removing vowels:\n",emp)
# reverse the string we got
rev_str = ""
for i in emp:
    rev_str = i + rev_str
print("String after reversing:\n",rev_str)


# # ------------------------------------------------------------------------------------------------------

# """-----------------------------Highest_Frequencies_in_the_word-------(if tie occurs)-------------------------------------"""

def highest_frequency_word(str_1):
    res = str_1.split()

    f = {}
    tie_list={}

    for i in res:
        f[i] = f.get(i, 0) + 1
    print(f)

    max_value= 0
    for i in f.values():
        if i > max_value:
            max_value = i
    print(max_value)


    for k,v in f.items():
        if v == max_value:
            tie_list[k]=v

    return tie_list
str_1 = "john went to the market john is in office john is in home is "
print(f"the_highest_frequency_in_the_list: {highest_frequency_word(str_1)}")


# ------------------------------------------------------------------------------------------------------

"""----------------------------------------  List comprehension  ----------------------------------"""
 