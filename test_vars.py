


a = 2

def f():
    global a
    print('dans f')
    a=43
    print(a)
    print('après f')

f()
print(a)


