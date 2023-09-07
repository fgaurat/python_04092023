


values = ["Value 01","Value 02","Value 03"]


for value in values: # for each
    print(value)



for i in range(len(values)):
    print(i,values[i])



print(list(range(len(values)))) # [0,1]

print(50*'-')


to_find = 122
values = [2,5,1,9,12,67,89]

found = False
for value in values:
    print(value)
    if value == to_find:
        print("ok")

        break
    print('ko')
else:
    pass

print("la fin")


print(50*'-')

def fib(n):    # write Fibonacci series up to n
    """
    Print a Fibonacci series up to n.
    """
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):    # write Fibonacci series up to n
    """
    Return a list containing the Fibonacci series up to n.
    """
    a, b = 0, 1
    results=[]
    while a < n:
        results.append(a)
        a, b = b, a+b

    return results

# Now call the function we just defined:
fib(4)


r = fib2(1000)
print(r)

for v in r:
    print(v)


r = fib2(n=34)
print(r)
r = fib2(12)
print(r)



def hello(name,firstName):

    print("Hello "+name+" "+firstName)


hello("GAURAT","Fred")
hello(firstName="Fred",name="GAURAT")




def add(*theArgs):
    print(theArgs)
    theResult = 0
    for i in theArgs:
        # theResult=theResult+i
        theResult+=i
    return theResult


theValues = [1,2,3,4]

theReturn1 = add(*theValues)
theReturn2 = add(10,20,30,40)

# theReturn = sum(theValues)
# print(theReturn1)# 10
print(theReturn2)# 100




s = "value 01"
s2 = "value 02"
s3 = "value 03"
print(s,s2,s3,sep=";")


print(*[1,2,3])


print(50*'-')

def hello(**info):

    print(info['firstName'])

hello(firstName="Fred",name="GAURAT")





def multAll2(theValues):
    theCalcul = []
    for i in theValues:
        theCalcul.append(i*2)
    return theCalcul
    

l = [2,3,4]
result  = multAll2(l) 
print(result) # [4,6,8]


result = map(lambda v:v*2,l)


print(list(result))
