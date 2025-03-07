#Lecture
'''
num=float(input("Enter a number:"))
if num<0:
    print(num,"is negative")

num=float(input("Enter another number:"))
if num>0:
    print(num, "is positive")
    print(num, "squared is",num*num)
    print("Bye")

num=float(input("Enter another number:"))
if num<0:
    print("It's negative")
else:
    print("It's not negative")

age=16
if age>=18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote")

from sqlalchemy.sql.functions import current_user

num=int(input("Enter a number:"))

if num>0:
    print('The number is positive.')
elif num<0:
    print("The number is negative.")
elif num==0:
    print("The number is zero.")

#while practice
current_num=1
while current_num<=5:
    print(current_num)
    current_num+=1

count=0
print("Staring...")
while count<10:
    print(count)
    count+=1 #also part of the while loop
    #not part of the while loop
print("Done")
'''
count=0
print("Staring...")
while count<10:
    print(count,"",end="") #end='' is make sure in the same line.
    count=count+1  #count+=1

print("Done") #or print ('\nDone')

colors=("red","yellow",'blue')
for item in colors:
    print(f"I have {item} colour.")

for num in range(5):
    print(num)

prompt=" Tell me something, and I will repeat it back to you:"
prompt+="\nEnter "quit" to end the program."

active=True
while active:
    message=input(prompt)

    if message=='quit':
        active=False
    else:
        print(message)
