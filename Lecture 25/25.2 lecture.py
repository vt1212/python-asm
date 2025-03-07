from conda.instructions import PRINT

name1='Anne'
name2='George'
#print("Good morning,",name1,"and",name2,"!")
print(f"good morning,{name1} and {name2}!")

string='Hello,Python!'
substring_list=string.split(',')
print(substring_list)

title="The Good, The Bad,and the Ugly"
print('Source String:',title)
print('Split using a space')
print(title.split(" "))
print('\nSplit using a comma')
print(title.split(","))

tuple_data=["apple", "banana", "cherry"]
result_string=" and ".join(tuple_data)#and qian hou need space
print(result_string)

text=" Hello World! "
left_stripped_text=text.lstrip()
print(left_stripped_text)

#Lecture 3
print('Enter your name: ')
name=input()
print(f'Hello,{name}.')

name=input('Enter your name: ')
print(f'Hello,{name}.')

age=int(input('Enter your age: '))
print('You are '+str(age)+'years old.')

name=input("Enter your age: ")
print(type(name))
#print(f"Hello, you are {age} years odl.")

age=int(input('Enter your age: '))
#print(type(age))
#print(f"Hello, you are {age} years old.")
print(age+3)


