

class DivBy12Error(Exception):

    def __init__(self) -> None:
        super().__init__("Division par 12 !!!!!")

def div(a,b):
    if b==12:
        # e = Exception("Division par 12 !!!!!")
        e = DivBy12Error()
        raise e
        
    c = a/b
    return c


def call_div(a,b):
    try:
        print("log avant")
        r = div(a,b)
    finally:
        print("log après")

    return r



def main():
    while True:
        b = int(input("Valeur de b : "))
        if b==-1:
            break
        try:    
            a = 2
            # c = a/b
            c = call_div(a,b)

            print(c)
        except ZeroDivisionError as e:
            print(e)
        except ValueError as e:
            print(e)
        except TypeError as e:
            print(e)
        except DivBy12Error as e:
            print("DivBy12Error",e)
        except Exception as e:
            print(e)

    print("la suite")


if __name__ == '__main__':
    main()
