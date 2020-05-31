name = input("Enter your name ==)")
age = input("Enter your age ==)")
print(f"Hello, {name}! and your age is {age}")

### Python list - good pratice to have similar data characteristics - not necessary to be same  
Alist = ['Apple', 'Orange', 'Grape']
print("The list ", Alist )

for i in range(5):
    print(i)

namesl = ["Charles", "Charlotte", "Charlene"]
for i in namesl:
    print(i)

### set in python - unique list of items, no orders in particular
oneset = set()
oneset.add(1)
oneset.add(3)
oneset.add(4)
oneset.add(3)
print(oneset)

### dictionary - set of records with key and values
ages = {"Charles":26, "Charlene": 24, "Charlotte": 22 }
print(ages)
print(ages["Charles"])

### function in Python
### from function-program-file import function-name
def insquare (x):
    return(x * x)

for i in range(5):
    print(f"Number {i} square is {insquare(i)}")

from functions import square
print(f"Number 121 square is {square(121)}")

