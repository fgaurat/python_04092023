
def main():
    a=2
    b=3.45


    s = "a:"+str(a)+" b:"+str(b)

    print(s)

    # f-string
    s = f"a:{a} b:{b}"
    print(s)
    s = f"{a=} {b=}"
    print(s)
    print(50*'-')
    a = 2
    b=3
    c = a/b

    print(f"{c*100:.2f}%")
    print(f"{c:.2%}")
    print("{1}   {0} = {2:.2%}".format(a,b,c))
    print(c)

    l = [10,20,30]

    print("{} {} {}".format(l[0],l[1],l[2]))
    print("{} {} {}".format(*l))
    
    print("Bonjour {name} {firstName}".format(name="GAURAT",firstName="Fred"))

    d = {
        "name":"GAURAT",
        "firstName":"Fred"
    }
    print("Bonjour {name} {firstName}".format(**d))
    print(f"Bonjour {d['name']} {d['firstName']}")



if __name__=='__main__':
    main()
