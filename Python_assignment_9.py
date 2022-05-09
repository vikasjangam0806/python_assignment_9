#Q-1 Python – Replace multiple words with K
# Python3 code to demonstrate working of 
# Replace multiple words with K
# Using join() + split() + list comprehension
  
# initializing string
test_str = 'Geeksforgeeks is best for geeks and CS'
  
# printing original string
print("The original string is : " + str(test_str))
  
# initializing word list 
word_list = ["best", 'CS', 'for']
  
# initializing replace word 
repl_wrd = 'gfg'
  
# Replace multiple words with K
# Using join() + split() + list comprehension
res = ' '.join([repl_wrd if idx in word_list else idx for idx in test_str.split()])
  
# printing result 
print("String after multiple replace : " + str(res)) 

#Q-2 Python | Permutation of a given string using inbuilt function 
# Function to find permutations of a given string
from itertools import permutations
  
def allPermutations(str):
       
     # Get all permutations of string 'ABC'
     permList = permutations(str)
  
     # print all permutations
     for perm in list(permList):
         print (''.join(perm))
        
# Driver program
if __name__ == "__main__":
    str = 'ABC'
    allPermutations(str)

#Q-3 Python | Check for URL in a String
# Python code to find the URL from an input string
# Using the regular expression
import re
  
def Find(string):
  
    # findall() has been used 
    # with valid conditions for urls in string
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,string)      
    return [x[0] for x in url]
      
# Driver Code
string = 'My Profile: https://github.com/vikasjangam0806/Python_assignment_8'
print("Urls: ", Find(string))

#Q-4 Execute a String of Code in Python
# Python program to illustrate use of exec to
# execute a given code as string.
 
# function illustrating how exec() functions.
def exec_code():
    LOC = """
def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact = fact*i
    return fact
print(factorial(5))
"""
    exec(LOC)
     
# Driver Code
exec_code()

#Q-5 String slicing in Python to rotate a string
# Function to rotate string left and right by d length 
  
def rotate(input,d): 
  
    # slice string in two parts for left and right 
    Lfirst = input[0 : d] 
    Lsecond = input[d :] 
    Rfirst = input[0 : len(input)-d] 
    Rsecond = input[len(input)-d : ] 
  
    # now concatenate two parts together 
    print ("Left Rotation : ", (Lsecond + Lfirst) )
    print ("Right Rotation : ", (Rsecond + Rfirst)) 
  
# Driver program 
if __name__ == "__main__": 
    input = 'mrchiku'
    d=2
    rotate(input,d) 

#Q-6 String slicing in Python to check if a string can become empty by recursive deletion
def checkEmpty(input, pattern): 
        
    # If both are empty  
    if len(input)== 0 and len(pattern)== 0: 
         return 'true'
    
    # If only pattern is empty 
    if len(pattern)== 0: 
         return 'true'
    
    while (len(input) != 0): 
  
        # find sub-string in main string 
        index = input.find(pattern) 
  
        # check if sub-string founded or not 
        if (index ==(-1)): 
          return 'false'
  
        # slice input string in two parts and concatenate 
        input = input[0:index] + input[index + len(pattern):]              
  
    return 'true'
    
# Driver program 
if __name__ == "__main__": 
    input ='GEEGEEKSKS'
    pattern ='GEEKS'
    print (checkEmpty(input, pattern))

#Q-7 Python Counter| Find all duplicate characters in string

from collections import Counter
  
def find_dup_char(input):
  
    # now create dictionary using counter method
    # which will have strings as key and their 
    # frequencies as value
    WC = Counter(input)
    j = -1
      
      
    # Finding no. of  occurrence of a character
    # and get the index of it.
    for i in WC.values():
        j = j + 1
        if( i > 1 ):
            print WC.keys()[j],
  
# Driver program
if __name__ == "__main__":
    input = 'geeksforgeeks'
    find_dup_char(input)

#Q-8 Python – Replace all occurrences of a substring in a string
# Python3 code to demonstrate working of 
# Swap Binary substring
# Using translate()
  
# initializing string
test_str = "geeksforgeeks"
  
# printing original string
print("The original string is : " + test_str)
  
# Swap Binary substring
# Using translate()
temp = str.maketrans("geek", "abcd")
test_str = test_str.translate(temp)
  
# printing result 
print("The string after swap : " + str(test_str)) 

#Q-9 Python – Extract Unique values dictionary values

# Python3 code to demonstrate working of 
# Extract Unique values dictionary values
# Using set comprehension + values() + sorted()
  
# initializing dictionary
test_dict = {'gfg' : [5, 6, 7, 8],
             'is' : [10, 11, 7, 5],
             'best' : [6, 12, 10, 8],
             'for' : [1, 2, 5]}
  
# printing original dictionary
print("The original dictionary is : " + str(test_dict))
  
# Extract Unique values dictionary values
# Using set comprehension + values() + sorted()
res = list(sorted({ele for val in test_dict.values() for ele in val}))
  
# printing result 
print("The unique values list is : " + str(res)) 

#Q-10 Python program to find the sum of all items in a dictionary

# Python3 Program to find sum of
# all items in a Dictionary
 
# Function to print sum
 
 
def returnSum(myDict):
 
    list = []
    for i in myDict:
        list.append(myDict[i])
    final = sum(list)
 
    return final
 
 
# Driver Function
dict = {'a': 100, 'b': 200, 'c': 300}
print("Sum :", returnSum(dict))