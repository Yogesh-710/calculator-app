from opration import do_addition, do_subtraction
from multiply import do_multiplication


def main():
    print('welcome to calculator app')
    print("""
          \n select the function from below options
          1. add
          2. subtract
          3. multiply
""")
    
    user_input = input("select the function")

    a = int(input('value of a'))
    b = int(input('value of b'))

    if user_input=="1":
        result = print(do_addition(a,b))
    elif user_input=="2":
        result = print(do_subtraction(a,b))
    elif user_input=="3":
        result = print(do_multiplication(a,b)) 

if __name__ == "__main__":
    main()   


