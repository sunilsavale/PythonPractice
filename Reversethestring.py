#Reverse the string
'''revers the string the using the for loop and the def'''

def reversed(string):
    #take a variable for empty string
    revers = ""
    for x in string:
        revers = x + revers
    print("revers string is:",revers )

#create a in

string = input("Enter the string:")
print("Enterred the string", string)
reversed(string)
    
    
