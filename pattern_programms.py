'''Practice on pattern program using input function '''

n = int(input("Enter a number of row:-"))

for i in range(1,n+1):
     for j in range(1,i+1):
          print("*",end="")
     print()


print(".....................................................................")

num = int(input("Enter a number of row:-"))

for i in range(num):
     print("* "*n)
