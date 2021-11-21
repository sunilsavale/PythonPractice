"""there many ways to revers the string"""
"""Way first by using the slicing operator"""

s = input("Enter some string:-")
print(s[::-1])

"""second way to reverse the string"""
s = input("Enter some string:-")
print(''.join(reversed(s))) # join is Concatenate any number of strings.

"""Another way to to reverse the string"""
s = input("Enter some string :-")
i = len(s)-1
name = ''

while i >= 0:
    name = name + s[i]
    i = i - 1
print(name)


"""Another way to revrse the string"""
def reversed(string):
    revers = ""
    for i in string:
        revers = i + revers
    print("Reversed string:", revers)
        
string = input("Enter a string:-")
print("Entered string is :", string)
reversed(string)


print("Reverse strings")
print("git practice")
print("Git practice 1")