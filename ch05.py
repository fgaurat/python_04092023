
import copy

l = []
l.append(12)
l.append(13)
l.append(14)
l.append(15)
print(l)
p = l.pop()
print(l)
print(p)

print(50*'-')

l1 = [10,20,30]
l2 = l1[:]

l1[0]=1000
print(l1)
print(l2)

print(50*'-')

l1 = [
    [10,20], #0
    [30,40], #1
    [50,60], #2
]
# l2 = l1[:]
l2 = copy.deepcopy(l1)

l1[1][0] = 1000

print(l1)
print(l2)

print(50*'-')

l = [2,3,4]
l2 = [x*2 for x in l]

print(l)
print(l2)


print(50*"-")

l =[
    "  value 01  ",
    "  value 02",
    "value 03  ",
]

l1= [s.strip() for s in l]
print(l1)


l1 = ["k1","k2","k3"]
l2 = ["v1","v2"]

l3 =zip(l1,l2)

print(l3)
print(list(l3))

print(50*'-')


t = 10,20,30
a,b,*c=12,54,67,78,45,23
print(a)
print(b)
print(c)

c = 1,

print(50*'-')

l = [1000,567,12,12,54,12,54,1000,76]
l = set(l)
print(l)
l.add(12)
print(l)
l.add(13)
print(l)
l = list(l)
print(l)

print(50*'-')

d = {
    "name":"GAURAT",
    "firstName":"Fred"
}

print(d['name'])

for k in d:
    print(k,d[k])

l =["value 01","value 02","value 03"]


for i in range(len(l)):
    print(i,l[i])


k,v = d.items()


for k,v in d.items():
    print(k,v)



for i,v in enumerate(l):
    print(i,v)

l =["value 01","value 02","value 03"]


v = "value 02"

if v in l:
    print("ok")