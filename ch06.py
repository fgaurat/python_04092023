import fibo as fi
import sys
# from fibo import *

# def fib(n):
#     print('fib')

def main():
    if len(sys.argv)>1:
        print(sys.argv)
        print(sys.argv[1])
        print(type(sys.argv[1]))
        print("ch06",__name__)
        intValue = int(sys.argv[1])
        fi.fib(intValue)
    else:
        print("manque param !")

if __name__ == "__main__":
    main()
