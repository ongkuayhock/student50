# Simple program
#

def summ (x):
    summ = 0
    for i in range(0,x+1):
        summ += i
    return(summ)

inp1 = input("Please Enter a numnber ")
inp2 = int(inp1)
if inp2 > 50:
    print("That is a high number")
else:
    print("That is a low number")
    
print( "Your number is : %s" % inp1)
print( "The sum is %s " % summ(inp2))

